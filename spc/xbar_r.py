import numpy as np


SPC_CONSTANTS = {
    2: {"A2": 1.880, "D3": 0.000, "D4": 3.267},
    3: {"A2": 1.023, "D3": 0.000, "D4": 2.574},
    4: {"A2": 0.729, "D3": 0.000, "D4": 2.282},
    5: {"A2": 0.577, "D3": 0.000, "D4": 2.114},
    6: {"A2": 0.483, "D3": 0.000, "D4": 2.004},
    7: {"A2": 0.419, "D3": 0.076, "D4": 1.924},
    8: {"A2": 0.373, "D3": 0.136, "D4": 1.864},
    9: {"A2": 0.337, "D3": 0.184, "D4": 1.816},
    10: {"A2": 0.308, "D3": 0.223, "D4": 1.777}
}


def calculate_xbar_r(data):

    data = np.array(data, dtype=float)

    subgroup_size = data.shape[1]

    if subgroup_size not in SPC_CONSTANTS:
        raise ValueError("Subgroup size must be between 2 and 10.")

    constants = SPC_CONSTANTS[subgroup_size]

    subgroup_means = np.mean(data, axis=1)

    subgroup_ranges = (
        np.max(data, axis=1)
        - np.min(data, axis=1)
    )

    xbar_bar = np.mean(subgroup_means)

    r_bar = np.mean(subgroup_ranges)

    xbar_ucl = (
        xbar_bar
        + constants["A2"] * r_bar
    )

    xbar_lcl = (
        xbar_bar
        - constants["A2"] * r_bar
    )

    r_ucl = (
        constants["D4"] * r_bar
    )

    r_lcl = (
        constants["D3"] * r_bar
    )

    return {
        "subgroup_means": subgroup_means.tolist(),
        "subgroup_ranges": subgroup_ranges.tolist(),

        "xbar": float(xbar_bar),
        "rbar": float(r_bar),

        "xbar_ucl": float(xbar_ucl),
        "xbar_lcl": float(xbar_lcl),

        "r_ucl": float(r_ucl),
        "r_lcl": float(r_lcl)
    }