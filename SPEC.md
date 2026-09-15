# RegenTwin / v0

## Purpose

RegenTwin is a Git-native state-chain format for regenerative agricultural assets.

## Core invariant

Every state after genesis MUST contain `previous_state_hash` equal to the verified `state_hash` of the immediately preceding state.

A state hash is computed from the complete state object excluding the `state_hash` field itself, using:

1. UTF-8 JSON
2. Object keys sorted lexicographically
3. Compact separators: `,` and `:`
4. SHA-256

The resulting identifier is encoded as:

```text
sha256:<hex-digest>
```

## Gate 0 acceptance criteria

- Three valid sequential states verify successfully.
- Sequence numbers are contiguous.
- All states reference the same `twin_id`.
- Every stored `state_hash` recomputes exactly.
- Every `previous_state_hash` references the preceding verified state.
- Retroactively modifying STATE-001 without rebuilding descendants invalidates the chain.

## Non-goals

Gate 0 does not establish legal ownership, regulatory compliance, biological causation, carbon-credit validity, blockchain anchoring, digital signatures, or post-quantum guarantees.
