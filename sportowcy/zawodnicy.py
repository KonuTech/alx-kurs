class Zawodnik:

    def __init__(self, imie: str, wzrost: int, waga: float) -> None:
        self.bmi = None
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def oblicz_bmi(self) -> float:
        return self.waga / (self.wzrost/100)**2
