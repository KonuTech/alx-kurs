odpowiedz_1 = "rowne liczby"
odpowiedz_2 = "najwieksza wartosc to liczba"
odpowiedz_3 = "blad"
liczba_1 = int(input(f"Wpisz liczbe 1:{chr(32)}"))
liczba_2 = int(input(f"Wpisz liczbe 2:{chr(32)}"))
liczba_3 = int(input(f"Wpisz liczbe 3:{chr(32)}"))

if (liczba_1 == liczba_2) and (liczba_2 == liczba_3):
    print(f"{odpowiedz_1}")
elif (liczba_1 > liczba_2) and (liczba_1 > liczba_3):
    print(f"{odpowiedz_2} {liczba_1}")
elif (liczba_2 > liczba_1) and (liczba_2 > liczba_3):
    print(f"{odpowiedz_2} {liczba_2}")
else:
    print(f"{liczba_3}")
