"""Declarative command specifications."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Mapping, Sequence


@dataclass
class CommandSpec:
    name: str
    flags: Mapping[str, type] = field(default_factory=dict)


def parse(spec: CommandSpec, argv: Sequence[str]) -> Dict[str, Any]:
    result: Dict[str, Any] = {"command": spec.name}
    index = 0
    while index < len(argv):
        token = argv[index]
        if not token.startswith("--"):
            raise ValueError(f"unexpected token {token!r}")
        key = token[2:]
        if key not in spec.flags:
            raise ValueError(f"unknown flag {key!r}")
        if index + 1 >= len(argv):
            raise ValueError(f"flag {key!r} requires a value")
        result[key] = spec.flags[key](argv[index + 1])
        index += 2
    return result
