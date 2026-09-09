import numpy as np


def calculate_imr(data):

    values = np.array(
        data,
        dtype=float
    )

    if len(values) < 2:

        raise ValueError(
            "At least 2 values are required."
        )


    mean_value = np.mean(values)

    moving_ranges = np.abs(
        np.diff(values)
    )

    mr_bar = np.mean(
        moving_ranges
    )


    i_ucl = (
        mean_value
        + 2.66 * mr_bar
    )

    i_lcl = (
        mean_value
        - 2.66 * mr_bar
    )


    mr_ucl = (
        3.267 * mr_bar
    )

    mr_lcl = 0


    return {

        "values":
            values.tolist(),

        "moving_ranges":
            moving_ranges.tolist(),

        "mean":
            float(mean_value),

        "i_ucl":
            float(i_ucl),

        "i_lcl":
            float(i_lcl),

        "mr_bar":
            float(mr_bar),

        "mr_ucl":
            float(mr_ucl),

        "mr_lcl":
            float(mr_lcl)
    }