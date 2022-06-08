import subprocess
from pathlib import Path

import pytask

from config import PLUGIN_SETS

THIS_DIR = Path(__file__).parent
INPUT = THIS_DIR / "input.py"
CONFIG = THIS_DIR / "config.yaml"

for ps in PLUGIN_SETS:
    name = "/".join(ps)
    working_dir = THIS_DIR / "pyroll" / name


    @pytask.mark.task(id=name)
    @pytask.mark.depends_on(INPUT)
    @pytask.mark.depends_on(CONFIG)
    @pytask.mark.produces(working_dir / "export.csv")
    @pytask.mark.produces(working_dir / "report.html")
    def task_run_pyroll(working_dir=working_dir, plugin_set=ps):
        result = subprocess.run(
            [
                "pyroll",
                "-c", CONFIG,
                *[e for p in plugin_set for e in ("-p", f"pyroll.{p}")],
                "input-py", "-f", INPUT,
                "solve",
                "export",
                "report",
            ],
            cwd=working_dir
        )

        result.check_returncode()
