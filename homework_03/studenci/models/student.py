class Student:

    def __init__(self, imie: str, nazwisko: str) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodaj_ocene(self, ocena):
        return self.oceny.append(ocena)

    def wypisz_oceny(self):
        for o, ocena in enumerate(self.oceny):
            print(ocena, end=", ")

    def policz_srednia(self):
        suma = 0
        liczebnosc_ocen = len(self.oceny)
        for o, ocena in enumerate(self.oceny):
            suma += ocena

        return suma / liczebnosc_ocen
