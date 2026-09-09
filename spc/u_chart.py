import numpy as np


def calculate_u_chart(defect_counts, sample_sizes):

    defect_counts = np.array(
        defect_counts,
        dtype=float
    )

    sample_sizes = np.array(
        sample_sizes,
        dtype=float
    )

    if len(defect_counts) != len(sample_sizes):
        raise ValueError(
            "Defect counts and sample sizes must have the same length."
        )

    if len(defect_counts) == 0:
        raise ValueError(
            "At least one sample is required."
        )

    if np.any(sample_sizes <= 0):
        raise ValueError(
            "All sample sizes must be greater than 0."
        )

    defects_per_unit = (
        defect_counts / sample_sizes
    )

    u_bar = (
        np.sum(defect_counts)
        / np.sum(sample_sizes)
    )

    ucl = (
        u_bar
        + 3
        * np.sqrt(
            u_bar / sample_sizes
        )
    )

    lcl = (
        u_bar
        - 3
        * np.sqrt(
            u_bar / sample_sizes
        )
    )

    lcl = np.maximum(
        lcl,
        0
    )

    return {

        "defects_per_unit":
            defects_per_unit.tolist(),

        "ubar":
            float(u_bar),

        "ucl":
            ucl.tolist(),

        "lcl":
            lcl.tolist()
    }