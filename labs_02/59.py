import random

liczba_do_odgadniecia = random.randint(1, 100)
print("Liczba do odgadniecia:\n", liczba_do_odgadniecia)

count = 1

while True:
    liczba_uzytkownika = int(input("Podaj liczbe:\n "))
    print("Liczba uzytkownika:\n", liczba_uzytkownika)

    if count < 5 and liczba_uzytkownika > liczba_do_odgadniecia:
        print(
            f"""
                Nie zgadles.
                Wykorzystales szans: {count} z 5 szans.
                Faktycznie liczba jest mniejsza:
                {liczba_do_odgadniecia} nie rowna sie {liczba_uzytkownika}
            """
        )
        count += 1

    elif count < 5 and liczba_uzytkownika < liczba_do_odgadniecia:
        print(
            f"""
                Nie zgadles.
                Wykorzystales szans: {count} z 5 szans.
                Faktycznie liczba jest wieksza:
                {liczba_do_odgadniecia} nie rowna sie {liczba_uzytkownika}
            """
        )
        count += 1

    else:
        print(
            f"""
                Koniec gry. Wygrales lub przegrales : )
                Wykorzystales szans: {count} z 5 szans.
            """
        )
        break
