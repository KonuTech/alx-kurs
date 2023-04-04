kontakty = []

while (True):

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec\n"))

    if menu == 1:

        imie = input("Podaj imie:\n")
        nazwisko = input("Podaj nazwisko:\n")
        telefon = input("Podaj telefon:\n")

        kontakt = [imie, nazwisko, telefon]
        kontakty.append(kontakt)
        print(
            f"""
                Dodany kontaky:
                    {kontakty}
            """
        )

    elif menu == 2:

        print(
            f"""
                Lista kontaktow:
            """
        )

        for kontakt in kontakty:

            print(
                f"""
                    {kontakty.index(kontakt)}: Imię: {kontakt[0]} Nazwisko: {kontakt[1]} Numer Tel.: {kontakt[2]}
                """
            )

    elif menu == 3:

        nazwisko = input("Podaj nazwisko do usuniecia:\n")

        znaleziono = False
        for kontakt in kontakty:
            if nazwisko == kontakt[1]:
                znaleziono = True
                kontakty.pop(kontakty.index(kontakt))
                print(
                    f"""
                        Kontakt {kontakt[1]} usunieto
                    """
                )

        if znaleziono == False:
            print("Nie znaleziono nazwiska")

    elif menu == 4:
        nazwisko = input("Podaj nazwisko:\n")
        noweImie = input("Podaj nowe imie:\n")
        noweNazwisko = input("Podaj nowe nazwisko:\n")
        nowyTelefon = input("Podaj nowy numer telefonu:\n")

        znaleziono = False
        for kontakt in kontakty:
            if nazwisko == kontakt[1]:
                znaleziono = True
                kontakt.insert(0, noweImie)
                kontakt.insert(1, noweNazwisko)
                kontakt.insert(2, nowyTelefon)

    elif menu == 5:
        break