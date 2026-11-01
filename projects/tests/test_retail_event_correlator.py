import unittest
from datetime import datetime, timedelta, timezone

from projects.retail_event_correlator import (
    EventType,
    SensorEvent,
    correlate_window,
)


class CorrelatorTests(unittest.TestCase):
    def setUp(self):
        self.start = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)

    def event(self, event_id, event_type, offset_seconds=0, confidence=0.8, zone="aisle-4"):
        return SensorEvent(
            event_id=event_id,
            event_type=event_type,
            occurred_at=self.start + timedelta(seconds=offset_seconds),
            zone=zone,
            source_id=f"sensor-{event_id}",
            confidence=confidence,
        )

    def test_creates_human_review_candidate_from_three_signal_types(self):
        candidate = correlate_window([
            self.event("v-1", EventType.VISION_ACTIVITY),
            self.event("r-1", EventType.RFID_MISMATCH, 20),
            self.event("w-1", EventType.SHELF_WEIGHT_CHANGE, 35),
        ])

        self.assertIsNotNone(candidate)
        self.assertEqual(candidate.disposition, "needs_human_review")
        self.assertFalse(candidate.is_automated_finding)
        self.assertEqual(candidate.zone, "aisle-4")
        self.assertEqual(len(candidate.event_ids), 3)

    def test_does_not_create_candidate_from_vision_and_only_one_other_signal(self):
        candidate = correlate_window([
            self.event("v-1", EventType.VISION_ACTIVITY),
            self.event("r-1", EventType.RFID_MISMATCH, 20),
        ])
        self.assertIsNone(candidate)

    def test_does_not_correlate_events_outside_the_time_window(self):
        candidate = correlate_window([
            self.event("v-1", EventType.VISION_ACTIVITY),
            self.event("r-1", EventType.RFID_MISMATCH, 20),
            self.event("w-1", EventType.SHELF_WEIGHT_CHANGE, 120),
        ], max_window_seconds=90)
        self.assertIsNone(candidate)

    def test_rejects_events_from_multiple_zones(self):
        with self.assertRaisesRegex(ValueError, "exactly one zone"):
            correlate_window([
                self.event("v-1", EventType.VISION_ACTIVITY),
                self.event("r-1", EventType.RFID_MISMATCH, 20),
                self.event("w-1", EventType.SHELF_WEIGHT_CHANGE, 30, zone="checkout"),
            ])

    def test_ignores_identical_duplicate_event_ids(self):
        vision = self.event("v-1", EventType.VISION_ACTIVITY)
        candidate = correlate_window([
            vision,
            vision,
            self.event("r-1", EventType.RFID_MISMATCH, 20),
            self.event("w-1", EventType.SHELF_WEIGHT_CHANGE, 30),
        ])
        self.assertIsNotNone(candidate)
        self.assertEqual(candidate.event_ids.count("v-1"), 1)

    def test_rejects_conflicting_duplicate_event_ids(self):
        with self.assertRaisesRegex(ValueError, "conflicting payloads"):
            correlate_window([
                self.event("same-id", EventType.VISION_ACTIVITY),
                self.event("same-id", EventType.RFID_MISMATCH, 10),
            ])

    def test_requires_timezone_aware_timestamps(self):
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            SensorEvent(
                event_id="naive",
                event_type=EventType.VISION_ACTIVITY,
                occurred_at=datetime(2026, 1, 1, 12, 0),
                zone="aisle-4",
                source_id="camera-1",
            )

    def test_confidence_must_be_between_zero_and_one(self):
        with self.assertRaisesRegex(ValueError, "between 0 and 1"):
            self.event("bad-confidence", EventType.VISION_ACTIVITY, confidence=1.5)

    def test_candidate_id_is_deterministic_for_the_same_events(self):
        events = [
            self.event("v-1", EventType.VISION_ACTIVITY),
            self.event("r-1", EventType.RFID_MISMATCH, 20),
            self.event("w-1", EventType.SHELF_WEIGHT_CHANGE, 30),
        ]
        first = correlate_window(events)
        second = correlate_window(reversed(events))
        self.assertEqual(first.candidate_id, second.candidate_id)


if __name__ == "__main__":
    unittest.main()
