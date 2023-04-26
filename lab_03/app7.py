from uczelnia.studenci_funkcje import *


FILE_NAME = "dane.txt"
DELIMITER = ","
ENCODING = "utf-8"


while True:

    menu = int(input("1-Dodaj Studenta\n2-Pokaz Studenta\n3-Usun Studenta\n4-Zmien Studenta\n5-Koniec\n"))

    if menu == 1:
        add_student(file_name=FILE_NAME, mode="a", encoding=ENCODING)

    elif menu == 2:
        pokaz_studenta(file_name=FILE_NAME, mode="r", encoding=ENCODING)

    elif menu == 3:
        usun_studenta(file_name=FILE_NAME, delimiter=DELIMITER, encoding=ENCODING)

    elif menu == 4:
        zmien_dane_studenta(file_name=FILE_NAME, delimiter=DELIMITER, encoding=ENCODING)

    elif menu == 4:
        break
