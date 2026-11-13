# Plume Embed

**Status: Released** - v0.4.2

Plume Embed is a compact on-device embedding lookup service. It ships a quantised
vector index, a small Python client and a command-line tool for building indexes
from pre-computed embeddings.

## Installation

```bash
pip install plume-embed
```

## Features

- Quantised index with sub-millisecond lookups on commodity laptops
- Streaming index builder that keeps peak memory bounded
- JSON and NumPy input adapters
- Deterministic re-ranking hooks for product search

## Repository layout

- `src/plume_embed/` - implementation
- `tests/` - test suite
- `examples/` - runnable examples

## Quick start

```python
from plume_embed import EmbeddingIndex

index = EmbeddingIndex(dim=384)
index.add("doc-1", vector)
print(index.search(vector, k=3))
```
