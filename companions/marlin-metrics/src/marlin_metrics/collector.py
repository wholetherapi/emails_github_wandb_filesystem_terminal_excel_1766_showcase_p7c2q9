"""Timing collector for column-store pipeline stages."""

from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Dict, Iterator, List


@dataclass
class Stage:
    name: str
    samples: List[float] = field(default_factory=list)

    @property
    def total(self) -> float:
        return sum(self.samples)

    @property
    def mean(self) -> float:
        return self.total / len(self.samples) if self.samples else 0.0


@dataclass
class Collector:
    run_name: str
    stages: Dict[str, Stage] = field(default_factory=dict)

    @contextmanager
    def stage(self, name: str) -> Iterator[Stage]:
        stage = self.stages.setdefault(name, Stage(name=name))
        started = time.perf_counter()
        try:
            yield stage
        finally:
            stage.samples.append(time.perf_counter() - started)
