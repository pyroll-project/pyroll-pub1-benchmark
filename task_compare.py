import pandas as pd
import pytask
from matplotlib import pyplot as plt

from config import PLUGIN_SETS, ROOT_DIR


@pytask.mark.depends_on([
    ROOT_DIR / "measure" / "data1.csv",
    ROOT_DIR / "measure" / "data2.csv",
    ROOT_DIR / "wicon" / "data.csv",
    *[
        ROOT_DIR / "pyroll" / "/".join(ps) / "export.csv"
        for ps in PLUGIN_SETS
    ]
])
@pytask.mark.produces([ROOT_DIR / "temperature.csv", ROOT_DIR / "torque.csv"])
def task_generate_data():
    measure1 = pd.read_csv(ROOT_DIR / "measure" / "data1.csv", index_col=0)
    measure2 = pd.read_csv(ROOT_DIR / "measure" / "data2.csv", index_col=0)
    wicon = pd.read_csv(ROOT_DIR / "wicon" / "data.csv", index_col=0)

    pyroll = {
        "/".join(ps): pd.read_csv(ROOT_DIR / "pyroll" / "/".join(ps) / "export.csv", index_col=0)
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


@pytask.mark.depends_on(ROOT_DIR / "torque.csv")
def task_plot_torque():
    df = pd.read_csv(ROOT_DIR / "torque.csv", index_col=0)

    plt.plot(df["measure1"].dropna(), c="gray")
    plt.plot(df["measure2"].dropna(), c="gray")
    plt.plot(df["wicon"].dropna(), c="black")

    for ps in PLUGIN_SETS:
        plt.plot(df["/".join(ps)].dropna())

    plt.savefig("torque.pdf")
    plt.close()


@pytask.mark.depends_on(ROOT_DIR / "temperature.csv")
def task_plot_temperature():
    df = pd.read_csv(ROOT_DIR / "temperature.csv", index_col=0)

    plt.plot(df["measure1"].dropna(), c="gray")
    plt.plot(df["measure2"].dropna(), c="gray")
    plt.plot(df["wicon"].dropna(), c="black")

    for ps in PLUGIN_SETS:
        plt.plot(df["/".join(ps)].dropna())

    plt.savefig("temperature.pdf")
    plt.close()
