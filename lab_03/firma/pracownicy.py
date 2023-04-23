class Pracownik:

    def __init__(self, imie: str, nazwisko: str, wynagrodzenie: int) -> None:
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wynagrodzenie = wynagrodzenie

    def getImie(self):
        return self.__imie

    def setImie(self, imie):
        self.__imie = imie

    def getNazwisko(self):
        return self.__nazwisko

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def getWynagrodzenie(self):
        return self.__wynagrodzenie

    def setWynagrodzenie(self, wynagrodzenie):
        self.__wynagrodzenie = wynagrodzenie

    def __str__(self):
        return f"\nImie: {self.__imie}\nNazwisko: {self.__nazwisko}\nWynagrodzenie: {self.__wynagrodzenie}\n"
