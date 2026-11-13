from .spec import CommandSpec, parse

SPEC = CommandSpec(name="demo", flags={"env": str, "replicas": int})
print(parse(SPEC, ["--env", "staging", "--replicas", "2"]))
