liczby = [-3, 6, -77, 2, -3, -9, 0, -1]


def homework_02_07(values: list):
    """
    Cwiczenie 62-4
    :param values:
    :return: None
    """
    print("Cwiczenie 62-4\n")

    minimal_index = 1

    while True:
        sorted = True
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                sorted = False
                if values[j] < values[minimal_index]:
                    minimal_index = j

            values[i], values[minimal_index] = values[minimal_index], values[i]

        if sorted is True:
            break

        print(values)


homework_02_07(values=liczby)


# dane = [5,2,4,1,3,8,1]
# print(dane)
#
# # pomysl II
# posortowane = []
#
# for j in range(len(dane)):
#     min = dane[0]
#     for i in range(1, len(dane)):
#         if dane[i] < min:
#             min = dane[i]
#
#     posortowane.append(min)
#     dane.remove(min)
#
#     print("#####################")
#     print(dane)
#     print(posortowane)


# pomysl I
# while(True):
#     posortowane = True
#     for i in range(len(dane)-1):
#         if dane[i] > dane[i+1]:
#             posortowane = False
#             tmp = dane[i]
#             dane[i] = dane[i+1]
#             dane[i+1] = tmp
#
#     if posortowane == True:
#         break
#
#     print(dane)
