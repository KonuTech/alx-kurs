from homework_03.firma_szkoleniowa.models.kurs import Kurs
from homework_03.firma_szkoleniowa.models.kursant import Kursant


def firma_szkoleniowa():
    listaKursow = []

    while True:

        menu = int(input(
            """
            1-dodaj kurs
            2-pokaz kursy
            3-usun kurs
            4-dodaj kursanta do kursu
            5-pokaz kurs wraz z kursantami
            6-usun kursanta z kursu
            7-koniec
            """
        ))

        if menu == 1:
            kurs = Kurs(
                nazwa=input("Podaj nazwe kursu:\n"),
                tryb=input("Podaj tryb kursu:\n")
            )

            listaKursow.append(kurs)

        elif menu == 2:
            for i, k in enumerate(listaKursow):
                print(
                    f"""
                        Kurs {i + 1}: 
                            nazwa:           {k.nazwa}
                            tryb:            {k.tryb}
                            lista kursantow: {k.listaKursantow}
                    """
                )
                # for x in k.listaKursantow:

        elif menu == 3:
            nazwa = input(
                "Podaj nazwe kursu:\n"
            )  # usuniecie kursu jest mozliwe tylko wtedy kiedy nie ma do niego przypisanych zadnych kursantow

            for i, k in enumerate(listaKursow):
                if len(k.listaKursantow) < 1 and k.nazwa == nazwa:
                    listaKursow.pop(i)
                    print(
                        f"""
                        Usunieto kurs {i + 1}:
                        """
                    )

        elif menu == 4:
            nazwa = input("Podaj nazwe kursu:\n")
            kursant = Kursant(
                imie=input("Podaj imie kursanta:\n"),
                nazwisko=input("Podaj nazwisko kursanta:\n")
            )

            for i, k in enumerate(listaKursow):
                print(k.nazwa, nazwa)
                if k.nazwa == nazwa:
                    k.listaKursantow.append(kursant)
                    print("Dodano Kursanta do Kursu")

        elif menu == 5:
            nazwa = input("Podaj nazwe kursu:\n")
            for i, k in enumerate(listaKursow):
                if k.nazwa == nazwa:
                    for j, kursant in enumerate(k.listaKursantow):
                        print(
                            f"""
                                Kurs {j + 1}: 
                                    imie:           {kursant.imie}
                                    nazwisko:       {kursant.nazwisko}
                            """
                        )

        elif menu == 6:
            nazwa = input("Podaj nazwe kursu:\n")
            nazwisko = input("Podaj nazwisko kursanta:\n")

            for i, kurs in enumerate(listaKursow):
                if kurs.nazwa == nazwa:
                    for j, kursant in enumerate(kurs.listaKursantow):
                        if kursant.nazwisko == nazwisko:
                            kurs.listaKursantow.remove(kursant)
                            print(
                                f"""
                                Usunieto Kursanta:
                                    Kurs {j + 1}: 
                                        imie:           {kursant.imie}
                                        nazwisko:       {kursant.nazwisko}
                                """
                            )

        elif menu == 7:
            break
