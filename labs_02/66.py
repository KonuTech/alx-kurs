import random


def get_list() -> list:
    """
    :return: list
    """

    values = []

    for i in range(0, 100):
        integer = random.randint(1, 100)
        values.append(integer)

    return values


def compute_operations() -> tuple:
    """
    :return: tuple
    """

    list_of_values = get_list()

    total = 0
    even_count = 0
    odd_count = 0

    maximum = list_of_values[0]
    minimum = list_of_values[0]

    for i in range(len(list_of_values)):
        if list_of_values[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if list_of_values[i] > maximum:
            maximum = list_of_values[i]
        if list_of_values[i] < minimum:
            minimum = list_of_values[i]

        total += list_of_values[i]

    average = total / len(list_of_values)

    return maximum, minimum, average, even_count, odd_count


results = compute_operations()
print(results)
