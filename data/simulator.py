import random


def generate_measurement():
    """
    Simulates measurements around 500 mL.

    Most measurements represent normal production.
    Occasionally an abnormal measurement is generated
    to test the SPC alarm system.
    """

    if random.random() < 0.90:
        value = random.normalvariate(500, 0.15)

    else:
        value = random.normalvariate(502, 0.15)

    return round(value, 2)


def generate_defective_count(sample_size=100):

    normal_rate = 0.04

    defective_count = sum(
        1
        for _ in range(sample_size)
        if random.random() < normal_rate
    )

    if random.random() < 0.08:

        defective_count = random.randint(
            10,
            18
        )

    return defective_count