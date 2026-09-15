import json
import sys
from pathlib import Path
from typing import Any, Dict, List

from .hash import compute_state_hash


class VerificationError(Exception):
    pass


def load_states(directory: Path) -> List[Dict[str, Any]]:
    files = sorted(directory.glob("STATE-*.json"))
    if not files:
        raise VerificationError("NO_STATES")
    return [json.loads(path.read_text(encoding="utf-8")) for path in files]


def verify_states(states: List[Dict[str, Any]]) -> str:
    twin_id = states[0].get("twin_id")
    previous_hash = None

    for expected_sequence, state in enumerate(states, start=1):
        if state.get("twin_id") != twin_id:
            raise VerificationError("TWIN_ID_MISMATCH")
        if state.get("sequence") != expected_sequence:
            raise VerificationError("SEQUENCE_MISMATCH")
        if state.get("previous_state_hash") != previous_hash:
            raise VerificationError("PREVIOUS_HASH_MISMATCH")

        recomputed = compute_state_hash(state)
        if state.get("state_hash") != recomputed:
            raise VerificationError("STATE_HASH_MISMATCH")

        previous_hash = state["state_hash"]

    return f"VERIFIED: {twin_id} ({len(states)} states)"


def verify_directory(directory: Path) -> str:
    return verify_states(load_states(directory))


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("twins/PLOT-001")
    try:
        print(verify_directory(target))
        return 0
    except VerificationError as exc:
        print(f"INVALID: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
