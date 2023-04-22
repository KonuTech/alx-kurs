class Auto:
    """
    A class creating an Auto object.
    """
    def __init__(self, marka: str, model: str, cena: float, kolor: str, silnik: float) -> None:
        """
        :param marka: str
        :param model: str
        :param cena: float
        :param kolor: str
        :param silnik: float
        """
        self.marka = marka
        self.model = model
        self.cena = cena
        self.kolor = kolor
        self.silnik = silnik


samochod_1 = Auto(cena=9999, kolor="niebieski", model="NX200", marka="Nissan", silnik=2.0)
samochod_2 = Auto(cena=8888, kolor="czerwony", model="NX100", marka="Nissan", silnik=2.5)
samochod_3 = Auto(cena=7777, kolor="zielony", model="NX300", marka="Nissan", silnik=1.5)


objects = [samochod_1, samochod_2, samochod_3]

for i, v in enumerate(objects):
    print(i, v)
    print(
        f"""
        samochod_{i+1}: 
            cena:   {v.cena}
            kolor:  {v.kolor}
            model:  {v.model}
            marka:  {v.marka}
            silnik: {v.silnik}
        """
    )
