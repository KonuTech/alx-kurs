#!/usr/bin/python
# TODO: baza sie zamyka po pierwszej funkcji


from dotenv import dotenv_values
import pymysql

tab = '\t'
new_line = '\n'
config = dotenv_values(".env")
table = config['TABLE']

conn = pymysql.connect(
    host=config["HOST"],
    user=config["USER"],
    password=config["PASSWORD"],
    database=config["DATABASE"],
    charset=config["CHARSET"],
    autocommit=config["AUTOCOMMIT"]
)


def dodaj(imie, nazwisko, pensja, table=table, conn=conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO {table} (imie, nazwisko, pensja) VALUES ('{imie}', '{nazwisko}', {pensja})")

        decyzja = input(f"Czy zatwierdzasz operacje T/N").upper()
        if decyzja == "T":
            conn.commit()
        else:
            conn.rollback()


def pokaz(table=table, conn=conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table}")
            dane = cur.fetchall()
            for r, row in enumerate(dane):
                print(f"""ID: {row[0]}{tab}IMIE: {row[1]}{tab}NAZWISKO: {row[2]}{tab}PENSJA: {row[3]}""")


def usun(id, table=table, conn=conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM {table} WHERE ID={id}")

        decyzja = input(f"Czy zatwierdzasz operacje T/N").upper()
        if decyzja == "T":
            conn.commit()
        else:
            conn.rollback()


def edytuj(id, imie, nazwisko, pensja, table=table, conn=conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {table} SET imie='{imie}', nazwisko='{nazwisko}', pensja={pensja} WHERE ID={id}")

        decyzja = input(f"Czy zatwierdzasz operacje T/N").upper()
        if decyzja == "T":
            conn.commit()
        else:
            conn.rollback()


def wyszukaj(imie, nazwisko, table=table, conn=conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table} WHERE imie='{imie}' AND nazwisko='{nazwisko}'")
            dane = cur.fetchall()
            for r, row in enumerate(dane):
                print(f"""ID: {row[0]}{tab}IMIE: {row[1]}{tab}NAZWISKO: {row[2]}{tab}PENSJA: {row[3]}""")


while True:

    menu = int(input(f"1-dodaj, 2-pokaz, 3-usun, 4-edytuj, 5-wyszukaj, 6-koniec\n"))

    if menu == 1:
        imie = input(f"Podaj imię:{new_line}")
        nazwisko = input(f"Podaj nazwisko:{new_line}")
        pensja = int(input(f"Podaj pensje pracownika:{new_line}"))

        dodaj(imie, nazwisko, pensja)

    elif menu == 2:

        pokaz()

    elif menu == 3:
        ID = int(input(f"Podaj id pracownika do usuniecia:{new_line}"))

        usun(id=ID, table=table)

    elif menu == 4:
        ID = int(input(f"Podaj id pracownika do usuniecia:{new_line}"))
        nowe_imie = input(f"Podaj nowe imię:{new_line}")
        nowe_nazwisko = input(f"Podaj nowe nazwisko:{new_line}")
        nowa_pensja = int(input(f"Podaj nową pensje pracownika:{new_line}"))

        edytuj(id=ID, imie=nowe_imie, nazwisko=nowe_nazwisko, pensja=nowa_pensja, table=table)

    elif menu == 5:
        fraza = input(f"Podaj imie i nazwisko do wyszukania:{new_line}")  # imie i nazwisko
        dane_osobowe = fraza.split()
        wyszukaj(imie=dane_osobowe[0], nazwisko=dane_osobowe[1], table=table)

    elif menu == 6:
        break
