import numpy as np


def calculate_p_chart(defectives, sample_sizes):

    defectives = np.array(
        defectives,
        dtype=float
    )

    sample_sizes = np.array(
        sample_sizes,
        dtype=float
    )

    if len(defectives) != len(sample_sizes):
        raise ValueError(
            "Defectives and sample sizes must have the same length."
        )

    proportions = (
        defectives / sample_sizes
    )

    p_bar = (
        np.sum(defectives)
        / np.sum(sample_sizes)
    )

    ucl = (
        p_bar
        + 3
        * np.sqrt(
            p_bar
            * (1 - p_bar)
            / sample_sizes
        )
    )

    lcl = (
        p_bar
        - 3
        * np.sqrt(
            p_bar
            * (1 - p_bar)
            / sample_sizes
        )
    )

    lcl = np.maximum(
        lcl,
        0
    )

    ucl = np.minimum(
        ucl,
        1
    )

    return {

        "proportions":
            proportions.tolist(),

        "pbar":
            float(p_bar),

        "ucl":
            ucl.tolist(),

        "lcl":
            lcl.tolist()
    }