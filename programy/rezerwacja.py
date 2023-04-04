def rezerwacja(kina: list, filmy: dict, cena_bilet: float) -> None:
    """
    :param kina: list
    :param filmy: dict
    :param cena_bilet: float
    :return: None
    """

    litery = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x",
              "c", "v", "b", "n", "m"]

    while True:

        print(
            f"""
                Lista kin:
                {", ".join(kina)}
                
            """
        )

        while True:
            try:
                id_kino = int(input("Podaj ID kina\n"))
                print(
                    f"""
                        Wybrane kino:
                        {kina[id_kino - 1]}
        
                    """
                )
                break
            except ValueError:
                print("PODAJ LICZBE CALKOWITA")
            except IndexError:
                print("NIEWLASCIWY INDEX WYBRANEGO KINA")

        print(
            f"""
                Lista filmow do wyboru:
                {", ".join(filmy[id_kino - 1])}
        
            """
        )

        while True:
            try:
                id_filmu = int(input("Podaj ID filmu\n"))
                print(
                    f"""
                        Wybrany film:
                        {filmy[id_kino - 1][id_filmu - 1]}
                
                    """
                )
                break
            except ValueError:
                print("PODAJ LICZBE CALKOWITA")
            except IndexError:
                print("NIEWLASCIWY INDEX WYBRANEGO KINA")

        while True:
            try:
                liczba_osob = int(input("Podaj liczbe osob\n"))
                print(
                    f"""
                        Podana liczba osob:
                        {liczba_osob}
                    """
                )
                break
            except ValueError:
                print("PODAJ LICZBE CALKOWITA")

        imie_zamawiajacego = input("Podaj swoje imie\n")

        for i in range(len(imie_zamawiajacego)):
            print(imie_zamawiajacego[i])
            try:
                # if imie_zamawiajacego[i] in set(litery):  # anna IN ['a', 'b', ... 'b']
                assert imie_zamawiajacego[i] in set(litery)
                print(
                    f"""
                            Kino: {kina[id_kino - 1]}
                            Film: {filmy[id_kino - 1][id_filmu - 1]}
                            Liczba osob: {liczba_osob}
                            Imie osoby rezerwujacej: {imie_zamawiajacego.capitalize()}
                            RAZEM DO ZAPLATY: {liczba_osob} * {cena_bilet} PLN = {liczba_osob * cena_bilet} PLN
                        """
                )
            except AssertionError:
                print("Niepoprawny znak")
