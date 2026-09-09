import numpy as np


SPC_CONSTANTS = {
    2: {"A3": 2.659, "B3": 0.000, "B4": 3.267},
    3: {"A3": 1.954, "B3": 0.000, "B4": 2.568},
    4: {"A3": 1.628, "B3": 0.000, "B4": 2.266},
    5: {"A3": 1.427, "B3": 0.000, "B4": 2.089},
    6: {"A3": 1.287, "B3": 0.030, "B4": 1.970},
    7: {"A3": 1.182, "B3": 0.118, "B4": 1.882},
    8: {"A3": 1.099, "B3": 0.185, "B4": 1.815},
    9: {"A3": 1.032, "B3": 0.239, "B4": 1.761},
    10: {"A3": 0.975, "B3": 0.284, "B4": 1.716}
}


def calculate_xbar_s(data):

    data = np.array(
        data,
        dtype=float
    )

    subgroup_size = data.shape[1]

    if subgroup_size not in SPC_CONSTANTS:
        raise ValueError(
            "Subgroup size must be between 2 and 10."
        )

    constants = SPC_CONSTANTS[
        subgroup_size
    ]

    subgroup_means = np.mean(
        data,
        axis=1
    )

    subgroup_std = np.std(
        data,
        axis=1,
        ddof=1
    )

    xbar_bar = np.mean(
        subgroup_means
    )

    s_bar = np.mean(
        subgroup_std
    )

    xbar_ucl = (
        xbar_bar
        + constants["A3"] * s_bar
    )

    xbar_lcl = (
        xbar_bar
        - constants["A3"] * s_bar
    )

    s_ucl = (
        constants["B4"] * s_bar
    )

    s_lcl = (
        constants["B3"] * s_bar
    )

    return {

        "subgroup_means":
            subgroup_means.tolist(),

        "subgroup_std":
            subgroup_std.tolist(),

        "xbar":
            float(xbar_bar),

        "sbar":
            float(s_bar),

        "xbar_ucl":
            float(xbar_ucl),

        "xbar_lcl":
            float(xbar_lcl),

        "s_ucl":
            float(s_ucl),

        "s_lcl":
            float(s_lcl)
    }