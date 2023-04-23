def open_file(file_name, mode="r", encoding="utf-8"):
    return open(file=file_name, mode=mode, encoding=encoding)


def close_file(file_name):
    file_name.close()


def add_student(file_name, mode="a", encoding="utf-8"):
    imie = input("Podaj imie Studenta\n")
    nazwisko = input("Podaj nazwisko Studenta\n")
    indeks = input("Podaj indeks Studenta\n")

    file = open_file(file_name, mode, encoding)
    file.write(f"{imie},{nazwisko},{indeks}\n")
    close_file(file)


def pokaz_studenta(file_name, mode="r", delimiter=",", encoding="utf-8"):
    nazwisko = input("Podaj nazwisko Studenta do pokazania\n")

    file = open_file(file_name, mode, encoding)
    row = file.readlines()

    for r, words in enumerate(row):
        if words.strip().split(delimiter)[1] == nazwisko:
            print(
                f"""
                    WIERSZ:             {r}
                    IMIE STUDENTA:      {words.strip().split(delimiter)[0]}
                    NAZWISKO STUDENTA:  {words.strip().split(delimiter)[1]}
                    INDEKS STUDENTA:    {words.strip().split(delimiter)[2]}
                """
            )

    close_file(file)


def usun_studenta(file_name, delimiter=",", encoding="utf-8"):
    nazwisko = input("Podaj nazwisko Studenta do usuniecia\n")

    file = open_file(file_name, mode="r", encoding=encoding)
    row = file.readlines()
    close_file(file)

    file = open_file(file_name, mode="w", encoding=encoding)
    for r, words in enumerate(row):
        if words.strip().split(delimiter)[1] != nazwisko:
            print(
                f"""
                    Student usuniety: {nazwisko}
                """
            )
            file.write(
                f"{words.strip().split(delimiter)[0]},{words.strip().split(delimiter)[1]},{words.strip().split(delimiter)[2]}\n"
            )

    close_file(file)


def zmien_dane_studenta(file_name, delimiter=",", encoding="utf-8"):
    nazwisko = input("Podaj stare nazwisko Studenta:\n")
    nowe_imie = input("Podaj nowe imie Studenta:\n")
    nowe_nazwisko = input("Podaj nowe nazwisko Studenta:\n")

    file = open_file(file_name, mode="r", encoding=encoding)
    row = file.readlines()
    close_file(file)

    file = open_file(file_name, mode="w", encoding=encoding)
    for r, words in enumerate(row):
        if words.strip().split(delimiter)[1] == nazwisko:
            print(
                f"""
                     Student edytowany: {nazwisko}
                 """
            )
            file.write(
                f"{nowe_imie},{nowe_nazwisko},{words.strip().split(delimiter)[2]}\n"
            )
        else:
            file.write(
                f"{words.strip().split(delimiter)[0]},{words.strip().split(delimiter)[1]},{words.strip().split(delimiter)[2]}\n"
            )

    close_file(file)
