# RegenTwin

Git-native digital twins for regenerative agricultural assets.

RegenTwin represents an agricultural asset as a deterministic chain of signed-ready JSON states. Each state cryptographically references the immediately preceding verified state.

## Gate 0

Gate 0 proves one invariant:

> No evidence-backed state transition can be altered retroactively without invalidating the chain.

The sample twin `CD-PLOT-001` contains three successive states. Verification uses canonical JSON plus SHA-256 and requires no external Python dependencies.

## Run

```bash
python -m regentwin.verify twins/PLOT-001
python -m unittest discover -s tests -v
```

Expected verification result:

```text
VERIFIED: CD-PLOT-001 (3 states)
```

## Scope

Gate 0 is a provenance prototype. It does not claim legal ownership, land-title validity, carbon-credit validity, RWA issuance, or post-quantum security. Those layers are intentionally separated for later gates.
