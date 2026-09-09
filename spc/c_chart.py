import numpy as np


def calculate_c_chart(defect_counts):

    defect_counts = np.array(
        defect_counts,
        dtype=float
    )

    if len(defect_counts) == 0:
        raise ValueError(
            "At least one defect count is required."
        )

    c_bar = np.mean(
        defect_counts
    )

    ucl = (
        c_bar
        + 3 * np.sqrt(c_bar)
    )

    lcl = (
        c_bar
        - 3 * np.sqrt(c_bar)
    )

    lcl = max(
        lcl,
        0
    )

    return {

        "defect_counts":
            defect_counts.tolist(),

        "cbar":
            float(c_bar),

        "ucl":
            float(ucl),

        "lcl":
            float(lcl)
    }