from marlin_metrics import Collector
from marlin_metrics.report import render_dashboard

collector = Collector("nightly")
with collector.stage("scan"):
    sum(range(100000))
print(render_dashboard([collector]))
