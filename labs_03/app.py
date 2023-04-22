from zatrudnieni.pracownicy import Pracownik

listaPracownikow = []

while True:

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec\n"))

    if menu == 1:
        pracownik = Pracownik(
            imie=input("Podaj imie:\n"),
            nazwisko=input("Podaj nazwisko:\n"),
            email=input("Podaj email:\n"),
            telefon=input("Podaj telefon:\n")
        )

        listaPracownikow.append(pracownik)

    elif menu == 2:
        for i, p in enumerate(listaPracownikow):
            print(
                f"""
                Pracownik {i+1}: 
                    imie:       {p.imie}
                    nazwisko:   {p.nazwisko}
                    email:      {p.email}
                    telefon:    {p.telefon}
                """
            )

    elif menu == 3:
        nazwisko = input("Podaj nazwisko:\n")

        for i, p in enumerate(listaPracownikow):
            if p.nazwisko == nazwisko:
                listaPracownikow.pop(i)
                print(
                    f"""
                    Usunieto pracownika {i+1}:
                    """
                )

    elif menu == 4:
        nazwisko = input("Podaj nazwisko do aktualizacji:\n")
        for i, p in enumerate(listaPracownikow):
            if p.nazwisko == nazwisko:
                    p.imie = input("Podaj nowe imie:\n")
                    p.nazwisko = input("Podaj nowe nazwisko:\n")
                    p.email = input("Podaj nowy email:\n")
                    p.telefon = input("Podaj nowy telefon:\n")

    elif menu == 5:
        print("Do widzenia.\n")
        break
