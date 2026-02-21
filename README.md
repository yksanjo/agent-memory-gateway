# agent-memory-gateway

Unified memory interface over vector, key-value, and relational backends.

## Scope

Memory APIs, retention windows, recall quality controls, and lineage.

## Capabilities

- Memory APIs, retention windows, recall quality controls, and lineage.
- Cross-store retrieval and consistency strategy with write contracts.
- Namespace and tenancy boundaries with strict access controls.
- Deterministic replay and evidence traceability for memory lookups.

## Repository Layout

- `src/main.py` entrypoint and lightweight service bootstrap
- `src/project_profile.py` canonical project metadata
- `src/service_contract.py` baseline domain contract shape
- `tests/` smoke and contract tests
- `docs/` architecture and roadmap

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest -q
python -m src.main
```
