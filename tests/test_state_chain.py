import copy
import unittest
from pathlib import Path

from regentwin.verify import VerificationError, load_states, verify_states


class RegenTwinGate0Tests(unittest.TestCase):
    def setUp(self):
        self.states = load_states(Path("twins/PLOT-001"))

    def test_valid_chain(self):
        self.assertEqual(
            verify_states(self.states),
            "VERIFIED: CD-PLOT-001 (3 states)",
        )

    def test_retroactive_state_change_is_detected(self):
        altered = copy.deepcopy(self.states)
        altered[0]["state"]["soil_carbon_percent"] = 9.99
        with self.assertRaisesRegex(VerificationError, "STATE_HASH_MISMATCH"):
            verify_states(altered)

    def test_broken_link_is_detected(self):
        altered = copy.deepcopy(self.states)
        altered[1]["previous_state_hash"] = "sha256:" + "0" * 64
        with self.assertRaisesRegex(VerificationError, "PREVIOUS_HASH_MISMATCH"):
            verify_states(altered)

    def test_sequence_gap_is_detected(self):
        altered = copy.deepcopy(self.states)
        altered[2]["sequence"] = 4
        with self.assertRaisesRegex(VerificationError, "SEQUENCE_MISMATCH"):
            verify_states(altered)


if __name__ == "__main__":
    unittest.main()
