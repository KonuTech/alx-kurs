from homework_02.homework_02 import *


# Variables for homework 02.06
word = "konstantynopolitańczykowianeczka"

# Variables for homework 02.08
kina = ["Cinema-City", "Multikino"]
filmy = {
    0: ["Matrix", "Avatar", "Shrek"],
    1: ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]
}
cena_bilet = 18.00

# Variables for homework 02.07
values = [-3, 6, -77, 2, -3, -9, 0, -1]

if __name__ == '__main__':
    homework_02_01()
    homework_02_02()
    homework_02_03(minimum=1, maximum=10, steps=10)
    homework_02_04(minimum=1, maximum=25, steps=20)
    homework_02_05(minimum=1, maximum=10, steps=2)
    homework_02_06(word)
    homework_02_07(values)
    homework_02_08(kina, filmy, cena_bilet)
    homework_02_09()
