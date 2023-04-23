FILE = "dane.txt"
MODE = "r"
ENCODING = "utf-8"


def open_file(file_name, mode="r", encoding="utf-8"):
    return open(file=file_name, mode=mode, encoding=encoding)


def close_file(file_name):
    file_name.close()


def read_file(file_name, mode, encoding):

    file = open_file(file_name, mode, encoding)
    row = file.readlines()

    for r, words in enumerate(row):
        print(r, words.strip().split(","))

    close_file(file)


def get_names(file_name, mode, encoding):
    file = open_file(file_name, mode, encoding)
    row = file.readlines()

    for r, words in enumerate(row):
        print(f"WIERSZ: {r} IMIE: {words.strip().split(',')[0]} MAIL: {words.strip().split(',')[2]}")

    close_file(file)


def write_rows(file_name, mode="a", encoding="utf-8"):
    imie = input("Podaj imie\n")
    wyplata = input("Podaj wyplate\n")
    mail = input("Podaj adres email\n")

    file = open_file(file_name, mode, encoding)
    file.write(f"{imie},{wyplata},{mail}\n")
    close_file(file)


if __name__ == '__main__':
    read_file(file_name=FILE, mode=MODE, encoding=ENCODING)
    get_names(file_name=FILE, mode=MODE, encoding=ENCODING)
    write_rows(file_name=FILE, mode="a", encoding="utf-8")
