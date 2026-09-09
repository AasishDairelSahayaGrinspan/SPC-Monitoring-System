import numpy as np


def calculate_np_chart(defectives, sample_size):

    defectives = np.array(
        defectives,
        dtype=float
    )

    if sample_size <= 0:
        raise ValueError(
            "Sample size must be greater than 0."
        )

    p_bar = (
        np.sum(defectives)
        / (
            len(defectives)
            * sample_size
        )
    )

    np_bar = (
        sample_size
        * p_bar
    )

    sigma = np.sqrt(
        sample_size
        * p_bar
        * (1 - p_bar)
    )

    ucl = (
        np_bar
        + 3 * sigma
    )

    lcl = (
        np_bar
        - 3 * sigma
    )

    lcl = max(
        lcl,
        0
    )

    return {

        "defectives":
            defectives.tolist(),

        "npbar":
            float(np_bar),

        "ucl":
            float(ucl),

        "lcl":
            float(lcl)
    }