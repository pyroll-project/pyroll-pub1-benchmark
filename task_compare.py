import numpy as np
import pandas as pd
import pytask
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

from config import PLUGIN_SETS, ROOT_DIR, PLUGINS, pretty_name, pretty_name_short, pyroll_model_key


@pytask.mark.depends_on([
    ROOT_DIR / "measure" / "data1.csv",
    ROOT_DIR / "measure" / "data2.csv",
    ROOT_DIR / "wicon" / "data.csv",
    *[
        ROOT_DIR / "pyroll" / pyroll_model_key(ps) / "export.csv"
        for ps in PLUGIN_SETS
    ]
])
@pytask.mark.produces([ROOT_DIR / "temperature.csv", ROOT_DIR / "torque.csv"])
def task_generate_data():
    measure1 = pd.read_csv(ROOT_DIR / "measure" / "data1.csv", index_col=0)
    measure2 = pd.read_csv(ROOT_DIR / "measure" / "data2.csv", index_col=0)
    wicon = pd.read_csv(ROOT_DIR / "wicon" / "data.csv", index_col=0)

    pyroll = {
        pyroll_model_key(ps): pd.read_csv(ROOT_DIR / "pyroll" / pyroll_model_key(ps) / "export.csv", index_col=0)
        for ps in PLUGIN_SETS
    }

    temperature = pd.concat(
        [
            measure1["temperature"],
            measure2["temperature"],
            wicon["temperature"],
            *[df["out_temperature"] - 273.15 for df in pyroll.values()]
        ],
        axis=1,
        keys=["measure1", "measure2", "wicon", *pyroll.keys()]
    ).sort_index()

    temperature.to_csv(ROOT_DIR / "temperature.csv")

    torque = pd.concat(
        [
            measure1["torque"] / 2,  # division by 2 due to single roll torque
            measure2["torque"] / 2,
            wicon["torque"] / 2,
            *[df["roll_torque"] for df in pyroll.values()]
        ],
        axis=1,
        keys=["measure1", "measure2", "wicon", *pyroll.keys()]
    ).sort_index()

    torque.to_csv(ROOT_DIR / "torque.csv")


for key, label in [
    ("temperature", r"Temperature $T$ in $\mathrm{K}$"),
    ("torque", r"Roll Torque $M$ in $\mathrm{Nm}$"),
]:
    @pytask.mark.task(id=key)
    @pytask.mark.depends_on(ROOT_DIR / f"{key}.csv")
    @pytask.mark.produces([
        ROOT_DIR / f"{key}.pdf",
        ROOT_DIR / f"{key}.png",
        ROOT_DIR / f"{key}.svg"
    ])
    def task_plot(data_key=key, yaxis_label=label):
        df = pd.read_csv(ROOT_DIR / f"{data_key}.csv", index_col=0)

        fig: plt.Figure = plt.figure(figsize=(9, 8))
        grid = fig.add_gridspec(3, 1, height_ratios=[1, 0.5, 0.001])
        ax: plt.Axes = fig.add_subplot(grid[0])

        ax.plot(df["measure1"].dropna(), label="Exp. Set 1", c="gray")
        ax.plot(df["measure2"].dropna(), label="Exp. Set 2", c="gray", ls="--")
        ax.plot(df["wicon"].dropna(), label="WICON", c="black")

        for ps in PLUGIN_SETS:
            ax.plot(df[pyroll_model_key(ps)].dropna(), label="PyRoll " + "/".join(pretty_name_short(p) for p in ps))

        fig.legend(loc="lower center", bbox_to_anchor=(0.5, 0.001), ncol=3, frameon=True)

        ax.set_xlabel("Roll Pass")
        ax.set_ylabel(yaxis_label)

        ax.set_xticks(range(0, len(df) + 1, 2))
        ax.set_xticklabels(range(0, len(df) // 2 + 1))

        fig.set_constrained_layout(True)

        fig.savefig(ROOT_DIR / f"{data_key}.pdf")
        fig.savefig(ROOT_DIR / f"{data_key}.png", dpi=600)
        fig.savefig(ROOT_DIR / f"{data_key}.svg")

        plt.close(fig)

for key, label in [
    ("temperature", r"Temperature $T$ in $\mathrm{K}$"),
    ("torque", r"Roll Torque $M$ in $\mathrm{Nm}$"),
]:
    for level_index, level_name in enumerate(PLUGINS.keys()):
        @pytask.mark.task(id=f"{key}-{level_name}")
        @pytask.mark.depends_on(ROOT_DIR / f"{key}.csv")
        @pytask.mark.produces([
            ROOT_DIR / f"{key}-{level_name}.pdf",
            ROOT_DIR / f"{key}-{level_name}.png",
            ROOT_DIR / f"{key}-{level_name}.svg"
        ])
        def task_plot(data_key=key, yaxis_label=label, level_name=level_name, level_index=level_index):
            df = pd.read_csv(ROOT_DIR / f"{data_key}.csv", index_col=0)

            fig: plt.Figure = plt.figure(figsize=(9, 5))
            grid = fig.add_gridspec(3, 1, height_ratios=[1, 0.1, 0.001])
            ax: plt.Axes = fig.add_subplot(grid[0])

            exp1 = ax.plot(df["measure1"].dropna(), label="Exp. Set 1", c="gray")
            exp2 = ax.plot(df["measure2"].dropna(), label="Exp. Set 2", c="gray", ls="--")
            wicon = ax.plot(df["wicon"].dropna(), label="WICON", c="black")

            for ps in PLUGIN_SETS:
                ax.plot(
                    df[pyroll_model_key(ps)].dropna(),
                    label="PyRoll " + "/".join(pretty_name_short(p) for p in ps),
                    c=f"C{PLUGINS[level_name].index(ps[level_index])}"
                )

            handles = exp1 + exp2 + wicon + [
                Line2D([], [], c=f"C{i}", label="PyRoll " + pretty_name_short(p))
                for i, p in enumerate(PLUGINS[level_name])
            ]

            fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.001),
                       ncol=(3 + len(PLUGINS[level_name])),
                       frameon=True)

            ax.set_title(f"Comparison of {pretty_name(level_name)}s")

            ax.set_xlabel("Roll Pass")
            ax.set_ylabel(yaxis_label)

            ax.set_xticks(range(0, len(df) + 1, 2))
            ax.set_xticklabels(range(0, len(df) // 2 + 1))

            fig.set_constrained_layout(True)

            fig.savefig(ROOT_DIR / f"{data_key}-{level_name}.pdf")
            fig.savefig(ROOT_DIR / f"{data_key}-{level_name}.png", dpi=600)
            fig.savefig(ROOT_DIR / f"{data_key}-{level_name}.svg")

            plt.close(fig)
