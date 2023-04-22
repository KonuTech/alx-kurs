from uczelnia.studenci import Student


listaStudentow = []

while True:

    menu = int(input(
        """
        1-dodaj studenta
        2-pokaz studentow
        3-usun studenta
        4-dodaj ocenę studentowi
        5-wypisz oceny studenta
        6-srednia studenta
        7-koniec\n
        """
    ))

    if menu == 1:
        student = Student(
            imie=input("Podaj imie:\n"),
            nazwisko=input("Podaj nazwisko:\n")
        )

        listaStudentow.append(student)

    elif menu == 2:
        for s, student in enumerate(listaStudentow):
            print(
                f"""
                    Student {s+1}: 
                        imie:   {student.imie}
                        wzrost: {student.nazwisko}
                        oceny:  {student.oceny}
                """
            )

    elif menu == 3:
        nazwisko = input("Podaj nazwisko studenta:\n")
        for s, student in enumerate(listaStudentow):
            if student.nazwisko == nazwisko:
                listaStudentow.pop(s)
                print(
                    f"""
                    Usunieto studenta {s+1}:
                        imie: {student.imie}
                        nazwisko: {student.nazwisko}
                    """
                )

    elif menu == 4:
        nazwisko = input("Podaj nazwisko studenta:\n")
        ocena = int(input("Podaj ocene:\n"))

        for s, student in enumerate(listaStudentow):
            if student.nazwisko == nazwisko:
                student.dodaj_ocene(ocena)
                print("Dodano ocene studentowi")

    elif menu == 5:
        nazwisko = input("Podaj nazwisko studenta:\n")

        for s, student in enumerate(listaStudentow):
            if student.nazwisko == nazwisko:
                print(f"Oceny studenta: {student.nazwisko}\n")
                student.wypisz_oceny()

    elif menu == 6:
        nazwisko = input("Podaj nazwisko studenta:\n")

        for s, student in enumerate(listaStudentow):
            if student.nazwisko == nazwisko:
                print(f"Srednia ocen studenta: {student.policz_srednia()}\n")

    elif menu == 7:
        break
