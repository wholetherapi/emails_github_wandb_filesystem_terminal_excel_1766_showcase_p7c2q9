from lumen_cli import CommandSpec, parse


def test_parse_casts_flags():
    spec = CommandSpec(name="deploy", flags={"replicas": int})
    assert parse(spec, ["--replicas", "3"])["replicas"] == 3
