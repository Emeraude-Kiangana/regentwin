import hashlib
import json
from typing import Any, Dict


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def compute_state_hash(state: Dict[str, Any]) -> str:
    payload = {k: v for k, v in state.items() if k != "state_hash"}
    digest = hashlib.sha256(canonical_json_bytes(payload)).hexdigest()
    return f"sha256:{digest}"
