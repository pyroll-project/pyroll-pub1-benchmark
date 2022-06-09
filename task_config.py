import itertools
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent

sys.path.append(ROOT_DIR)

PLUGINS: dict[str, list[str]] = {
    "force_model": [
        "",
        "hensel_power_and_labour",
        "sims_power_and_labour",
    ],
    "spreading_model": [
        "",
        "hill_spreading",
        "wusatowski_spreading",
    ],
    "equivalent_rectangle_method": [
        "",
        "lendl_equivalent_method",
    ],
}

PLUGIN_SETS: list[tuple[str]] = list(itertools.product(*PLUGINS.values()))


def pretty_name(name: str):
    return " ".join(
        (s.title() if s else "Base")
        for s in name.split("_")
    )


def pretty_name_short(name: str):
    if not name:
        return "Base"
    return name.split("_")[0].title()


def pyroll_model_key(plugin_set: tuple[str]):
    return "/".join((p if p else "base") for p in plugin_set)
