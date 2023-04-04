import random


def get_values() -> list:
    scalars = []

    for s in range(0, 10):
        scalars.append(random.randint(1, 10))

    return scalars


def remove_item(series: list, double: list) -> list:
    results = []

    for v in series:
        if v not in set(double):
            results.append(v)

    return results
