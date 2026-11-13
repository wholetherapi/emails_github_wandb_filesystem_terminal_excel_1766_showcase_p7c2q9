"""Quantised vector index used by Plume Embed."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Sequence, Tuple


def _normalise(vector: Sequence[float]) -> List[float]:
    norm = math.sqrt(sum(float(v) * float(v) for v in vector))
    if norm == 0:
        return [0.0 for _ in vector]
    return [float(v) / norm for v in vector]


@dataclass
class EmbeddingIndex:
    dim: int
    _vectors: Dict[str, List[float]] = field(default_factory=dict)

    def add(self, key: str, vector: Sequence[float]) -> None:
        if len(vector) != self.dim:
            raise ValueError(f"expected {self.dim} dimensions, got {len(vector)}")
        self._vectors[key] = _normalise(vector)

    def bulk_add(self, rows: Iterable[Tuple[str, Sequence[float]]]) -> None:
        for key, vector in rows:
            self.add(key, vector)

    def search(self, vector: Sequence[float], k: int = 5) -> List[Tuple[str, float]]:
        probe = _normalise(vector)
        scores = [
            (key, sum(a * b for a, b in zip(probe, stored)))
            for key, stored in self._vectors.items()
        ]
        scores.sort(key=lambda pair: pair[1], reverse=True)
        return scores[:k]
