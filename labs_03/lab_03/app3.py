from sportowcy.zawodnicy import Zawodnik


listaZawodnikow = []

while True:

    menu = int(input(
        """
        1-dodaj Zawodnika
        2-pokaz Zawodnikow
        3-oblicz BMI Zawodnika
        4-koniec
        """
    ))

    if menu == 1:
        zawodnik = Zawodnik(
            imie=input("Podaj imie Zawodnika:\n"),
            wzrost=int(input("Podaj wzrost Zawodnika:\n")),
            waga=float(input("Podaj wage Zawodnika:\n"))
        )

        listaZawodnikow.append(zawodnik)

    elif menu == 2:
        for z, zawodnik in enumerate(listaZawodnikow):
            print(
                f"""
                    Zawodnik {z+1}: 
                        imie:   {zawodnik.imie}
                        wzrost: {zawodnik.wzrost}
                        waga:   {zawodnik.waga}
                """
            )

    elif menu == 3:
        imie = input("Podaj imie Zawodnika:\n")
        for z, zawodnik in enumerate(listaZawodnikow):
            if zawodnik.imie == imie:
                print(
                    f"""
                        Zawodnik {z+1}: 
                            imie:   {zawodnik.imie}
                            wzrost: {zawodnik.wzrost}
                            waga:   {zawodnik.waga}
                            BMI:    {zawodnik.oblicz_bmi()}
                    """
                )

    elif menu == 4:
        break
