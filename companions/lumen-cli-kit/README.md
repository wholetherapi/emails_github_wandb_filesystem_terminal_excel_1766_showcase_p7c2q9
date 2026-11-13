# Lumen CLI Kit

**Status: Released** - v2.0.1

Lumen CLI Kit helps internal platform teams generate typed command trees and
configuration loaders without hand-writing argument parsing boilerplate.

## Installation

```bash
pip install lumen-cli-kit
```

## Included

- `src/lumen_cli/spec.py` - declarative command specification
- `src/lumen_cli/__main__.py` - reference runner
- `tests/` - unit tests

## Example

```python
from lumen_cli import CommandSpec, parse

spec = CommandSpec(name="deploy", flags={"env": str, "replicas": int})
print(parse(spec, ["--env", "prod", "--replicas", "3"]))
```
