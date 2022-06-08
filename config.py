import itertools
from pathlib import Path

ROOT_DIR = Path(__file__).parent

PLUGINS = [
    ["hensel_power_and_labour", "sims_power_and_labour"],
    ["hill_spreading", "wusatowski_spreading", "sander_spreading"],
]

PLUGIN_SETS = list(itertools.product(*PLUGINS))
