import random


integer = random.randint(1, 100)
list_of_values = []
suma = 0

for i in range(0, 100):
    list_of_values.append(random.randint(1, 100))


_max = list_of_values[0]
_min = list_of_values[0]

for i in range(len(list_of_values)):
    if list_of_values[i] > _max:
        _max = list_of_values[i]
    if list_of_values[i] < _min:
        _min = list_of_values[i]

    suma += list_of_values[i]

srednia = suma / len(list_of_values)

print(
    f"""
        Lista wartosci to: {list_of_values}
        Min to: {_min}
        Max to: {_max}
        Suma to: {suma}
        Srednia to: {srednia}
    """
)
