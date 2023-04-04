import random


def get_values(minimum: int, maximum: int, steps: int) -> list:
    """
    :param minimum: int
    :param maximum: int
    :return: list
    """

    scalars = []

    for s in range(0, steps):
        scalars.append(random.randint(minimum, maximum))

    return scalars


def remove_item(series: list, double: list) -> list:
    """
    :param series: list
    :param double: list
    :return: list
    """
    results = []

    for v in series:
        if v not in set(double):
            results.append(v)

    return results
