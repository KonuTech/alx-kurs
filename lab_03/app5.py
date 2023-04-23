from firma.pracownicy import Pracownik

listaPracownikow = []

while True:

    menu = int(input("1 - dodaj pracownika\n"
                     "2 - pokaz wszystkich pracownikow\n"
                     "3 - usun pracownika\n"
                     "4 - zmiana wynagrodzenia\n"
                     "5 - koniec\n"
                     ))

    if menu == 1:
        zatrudniony = Pracownik(
            imie=input("Podaj imie:\n"),
            nazwisko=input("Podaj nazwisko:\n"),
            wynagrodzenie=int(input("Podaj wysokosc wynagrodzenia:\n"))
        )

        listaPracownikow.append(zatrudniony)

    elif menu == 2:
        for p, pracownik in enumerate(listaPracownikow):
            print(pracownik)

    elif menu == 3:
        nazwisko = input("Podaj nazwisko:\n")

        for p, pracownik in enumerate(listaPracownikow):
            if pracownik.getNazwisko() == nazwisko:
                listaPracownikow.pop(p)

    elif menu == 4:
        nazwisko = input("Podaj nazwisko:\n")
        wynagrodzenie = int(input("Podaj wysokosc nowego wynagrodzenia:\n"))

        for p, pracownik in enumerate(listaPracownikow):
            if pracownik.getNazwisko() == nazwisko:
                pracownik.setWynagrodzenie(wynagrodzenie)

    elif menu == 5:
        break
