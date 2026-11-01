from datetime import datetime, timedelta, timezone
import json

from projects.retail_event_correlator import (
    EventType,
    SensorEvent,
    candidate_to_dict,
    correlate_window,
)


def main() -> None:
    start = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    synthetic_events = [
        SensorEvent("cam-001", EventType.VISION_ACTIVITY, start, "aisle-4", "camera-edge-01", 0.91),
        SensorEvent("rfid-002", EventType.RFID_MISMATCH, start + timedelta(seconds=18), "aisle-4", "rfid-gate-02", 0.87),
        SensorEvent("scale-003", EventType.SHELF_WEIGHT_CHANGE, start + timedelta(seconds=31), "aisle-4", "shelf-scale-04", 0.82),
    ]

    candidate = correlate_window(synthetic_events)
    output = {
        "candidate": candidate_to_dict(candidate) if candidate else None,
        "notice": (
            "Synthetic demonstration only. A candidate is a request for authorized "
            "human review, not a finding of wrongdoing."
        ),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
