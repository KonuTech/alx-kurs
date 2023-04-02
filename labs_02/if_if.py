l_1 = [2, 5, 8, 3]
l_2 = [9, 0, 1, 2]


for i in range(len(l_1)):
    # print(l_1[i])
    for k in range(len(l_2)):
        # print(l_2[k])
        if l_1[i] == l_2[k]:
            print(True, i, k)


