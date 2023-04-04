from programy import rezerwacja as programy


kina = ["Cinema-City", "Multikino"]
filmy = {
    0: ["Matrix", "Avatar", "Shrek"],
    1: ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]
}
cena_bilet = 18.00

programy.rezerwacja(kina, filmy, cena_bilet)
