"""Render collected timings as an operator dashboard."""

from __future__ import annotations

from typing import Iterable

from .collector import Collector


def render_dashboard(collectors: Iterable[Collector]) -> str:
    lines = ["stage	mean_ms	total_ms"]
    for collector in collectors:
        for stage in collector.stages.values():
            lines.append(f"{stage.name}\t{stage.mean * 1000:.2f}\t{stage.total * 1000:.2f}")
    return "\n".join(lines)
