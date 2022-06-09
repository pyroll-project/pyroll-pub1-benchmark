import subprocess
import pytask

from config import PLUGIN_SETS, ROOT_DIR, pyroll_model_key

INPUT = ROOT_DIR / "input.py"
CONFIG = ROOT_DIR / "config.yaml"

for ps in PLUGIN_SETS:
    name = pyroll_model_key(ps)
    working_dir = ROOT_DIR / "pyroll" / name


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
                *[e for p in plugin_set for e in ("-p", f"pyroll.{p}") if p],
                "input-py", "-f", INPUT,
                "solve",
                "export",
                "report",
            ],
            cwd=working_dir
        )

        result.check_returncode()
