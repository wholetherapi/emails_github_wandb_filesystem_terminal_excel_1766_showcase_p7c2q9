from marlin_metrics import Collector


def test_stage_accumulates_samples():
    collector = Collector(run_name="demo")
    with collector.stage("decode") as stage:
        pass
    with collector.stage("decode") as stage:
        pass
    assert len(stage.samples) == 2
    assert stage.mean >= 0
