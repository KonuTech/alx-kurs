import random


l_1 = []
l_2 = []
listy = [l_1, l_2]

for lista in listy:
    for i in range(10):
        print("Losuje jedna liczbe z przedzialu <1;10>\n")
        n = random.randint(1, 10)

        print(
            f"""
                Wylosowana liczba to: {n}
            """
        )
        lista.append(n)
    print(
        f"""
            Dlugosc listy to: {len(lista)}
        """
    )

print(listy)

for lista in range(len(listy)-1):  # [0, 1]
    # print(listy[lista])
    print(range(len(listy)-1))
    for i in range(len(listy[lista])):  # [0, ... , 9]
        # print(listy[lista][i])
        for k in range(len(listy[lista+1])):  # [0, ... , 9]
            # print(listy[lista][k])
            if listy[lista][i] == listy[lista+1][k]:
                print(True, listy[lista][i], listy[lista+1][k])
