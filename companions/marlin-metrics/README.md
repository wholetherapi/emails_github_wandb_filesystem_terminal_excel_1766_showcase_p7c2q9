# Marlin Metrics

**Status: Released** - v1.3.0

Marlin Metrics is a lightweight instrumentation toolkit for streaming column-store
pipelines. It records per-operator timings and renders a compact dashboard that
operators can attach to release notes.

## Installation

```bash
pip install marlin-metrics
```

## What is included

- `src/marlin_metrics/collector.py` - low-overhead timing collector
- `src/marlin_metrics/report.py` - dashboard renderer
- `tests/` - unit tests
- `examples/` - sample integration

## Usage

```python
from marlin_metrics import Collector

with Collector("ingest").stage("decode") as stage:
    decode_batch(batch)
```
