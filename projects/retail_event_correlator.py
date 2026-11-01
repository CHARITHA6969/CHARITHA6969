"""Synthetic, human-review-first sensor event correlation prototype.

This module deliberately does not identify people, infer intent, or label an event
as theft. It only groups a small set of synthetic signals into a review candidate.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Iterable


class EventType(str, Enum):
    VISION_ACTIVITY = "vision_activity"
    RFID_MISMATCH = "rfid_mismatch"
    SHELF_WEIGHT_CHANGE = "shelf_weight_change"
    POS_EXCEPTION = "pos_exception"


CORROBORATING_TYPES = {
    EventType.RFID_MISMATCH,
    EventType.SHELF_WEIGHT_CHANGE,
    EventType.POS_EXCEPTION,
}


@dataclass(frozen=True, slots=True)
class SensorEvent:
    event_id: str
    event_type: EventType
    occurred_at: datetime
    zone: str
    source_id: str
    confidence: float | None = None

    def __post_init__(self) -> None:
        if not self.event_id.strip():
            raise ValueError("event_id must not be empty")
        if not self.zone.strip():
            raise ValueError("zone must not be empty")
        if not self.source_id.strip():
            raise ValueError("source_id must not be empty")
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True, slots=True)
class IncidentCandidate:
    candidate_id: str
    zone: str
    event_ids: tuple[str, ...]
    signal_types: tuple[str, ...]
    window_start: datetime
    window_end: datetime
    disposition: str = "needs_human_review"
    is_automated_finding: bool = False


def correlate_window(
    events: Iterable[SensorEvent],
    *,
    max_window_seconds: float = 90.0,
) -> IncidentCandidate | None:
    """Return a review candidate when independent signals overlap in one zone.

    Requirements:
    - one zone per input window;
    - the complete time span must fit inside max_window_seconds;
    - a vision activity and at least two distinct corroborating signal types.

    Duplicate event IDs with identical payloads are ignored. Conflicting payloads
    for the same ID are rejected to avoid silently corrupting the event history.
    """
    if max_window_seconds <= 0:
        raise ValueError("max_window_seconds must be greater than zero")

    unique_events: dict[str, SensorEvent] = {}
    for event in events:
        previous = unique_events.get(event.event_id)
        if previous is not None and previous != event:
            raise ValueError(f"conflicting payloads for event_id: {event.event_id}")
        unique_events[event.event_id] = event

    if not unique_events:
        return None

    ordered = sorted(
        unique_events.values(),
        key=lambda item: (item.occurred_at, item.event_id),
    )

    zones = {event.zone for event in ordered}
    if len(zones) != 1:
        raise ValueError("correlate_window accepts events from exactly one zone")

    start = ordered[0].occurred_at
    end = ordered[-1].occurred_at
    if end - start > timedelta(seconds=max_window_seconds):
        return None

    types = {event.event_type for event in ordered}
    corroborating = types.intersection(CORROBORATING_TYPES)
    if EventType.VISION_ACTIVITY not in types or len(corroborating) < 2:
        return None

    event_ids = tuple(event.event_id for event in ordered)
    fingerprint = hashlib.sha256(
        json.dumps(event_ids, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:12]

    return IncidentCandidate(
        candidate_id=f"review-{fingerprint}",
        zone=ordered[0].zone,
        event_ids=event_ids,
        signal_types=tuple(sorted(event_type.value for event_type in types)),
        window_start=start.astimezone(timezone.utc),
        window_end=end.astimezone(timezone.utc),
    )


def candidate_to_dict(candidate: IncidentCandidate) -> dict[str, object]:
    """Convert a candidate to a JSON-friendly structure."""
    payload = asdict(candidate)
    payload["window_start"] = candidate.window_start.isoformat()
    payload["window_end"] = candidate.window_end.isoformat()
    return payload
