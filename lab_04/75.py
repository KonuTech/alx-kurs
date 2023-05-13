from tkinter import *


class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email


def test():
    print("test !!!")


lista_kontaktow = []

def dodaj_kontakt(lista):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email =entry_email.get()
    kontakt = Kontakt(imie, nazwisko, telefon, email)
    lista.append(kontakt)

    for k, kontakt in enumerate(lista):
        print(
            f"""
            List of Contacts:
            ID: {k + 1}
            IMIE: {kontakt.imie}
            NAZWISKO: {kontakt.nazwisko}
            TELEFON: {kontakt.telefon}
            EMAIL: {kontakt.email}
            """
        )

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)

    # entry_imie.focus()
    # listbox_lista_kontaktow()


def pokaz_liste_kontaktow(lista):
    listbox_lista_kontaktow.delete(0, END)
    for i, kontakt in enumerate(lista):
        listbox_lista_kontaktow.insert(i, f"{kontakt.imie} {kontakt.nazwisko}")

def podaj_indeks():
    i = listbox_lista_kontaktow.index(ACTIVE)

    return i

def usun_kontakt(lista):
    aktywny_indeks = podaj_indeks()
    lista.pop(aktywny_indeks)
    pokaz_liste_kontaktow(lista)


def pokaz_szczegoly_kontaktu(lista):
    aktywny_indeks = podaj_indeks()
    aktywny_kontakt = lista[aktywny_indeks]
    label_imie_output_wyswietl.config(text=aktywny_kontakt.imie)
    label_nazwisko_output_wyswietl.config(text=aktywny_kontakt.nazwisko)
    label_telefon_output_wyswietl.config(text=aktywny_kontakt.telefon)
    label_email_output_wyswietl.config(text=aktywny_kontakt.email)


def edytuj_kontakt(lista):
    aktywny_indeks = podaj_indeks()
    aktywny_kontakt = lista[aktywny_indeks]
    entry_imie.delete(0, END)
    entry_imie.insert(0, aktywny_kontakt.imie)
    entry_nazwisko.delete(0, END)
    entry_nazwisko.insert(0, aktywny_kontakt.nazwisko)
    entry_telefon.delete(0, END)
    entry_telefon.insert(0, aktywny_kontakt.telefon)
    entry_email.delete(0, END)
    entry_email.insert(0, aktywny_kontakt.email)

    entry_dodaj_kontakt.config(text="Zmien kontakt", command=lambda: zmien_kontakt(lista_kontaktow))

def zmien_kontakt(lista):
    aktywny_indeks = podaj_indeks()
    aktywny_kontakt = lista[aktywny_indeks]

    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    stary_kontakt = lista_kontaktow[aktywny_indeks]
    stary_kontakt.imie = imie
    stary_kontakt.nazwisko = nazwisko
    stary_kontakt.telefon = telefon
    stary_kontakt.email = email

    # lista.insert(aktywny_indeks, kontakt)

    entry_dodaj_kontakt.config(text="Dodaje kontakt", command=lambda: dodaj_kontakt(lista))

    pokaz_liste_kontaktow(lista)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)

    entry_email.focus()



root = Tk()
root.geometry("700x300")
root.title("Aplikacja kontaktowa")

ramka_lewa = Frame(root)
ramka_prawa = Frame(root)
ramka_dolna = Frame(root)

ramka_lewa.grid(row=0, column=0, pady=(20, 20), padx=20)
ramka_prawa.grid(row=0, column=1, sticky=N, pady=20)
ramka_dolna.grid(row=1, column=0, columnspan=2, sticky=W, padx=20)

# definicja obiektow ramki lewej
label_lista_kontaktow = Label(ramka_lewa, text="Lista kontaktow")

listbox_lista_kontaktow = Listbox(ramka_lewa)

button_pokaz_kontakty = Button(ramka_lewa, text="Pokaz kontakty", command=lambda: pokaz_liste_kontaktow(lista_kontaktow))
button_pokaz_kontakt = Button(ramka_lewa, text="Pokaz szczegoly kontaktu", command=lambda: pokaz_szczegoly_kontaktu(lista_kontaktow))
button_usun_kontakt = Button(ramka_lewa, text="Usun kontakt", command=lambda: usun_kontakt(lista_kontaktow))
button_edytuj_kontakt = Button(ramka_lewa, text="Edytuj kontakt", command=lambda: edytuj_kontakt(lista_kontaktow))

# ramka_lewa gridowanie
label_lista_kontaktow.grid(row=0, column=0, columnspan=3)

listbox_lista_kontaktow.grid(row=1, column=0, columnspan=3)

button_pokaz_kontakty.grid(row=2, column=0, columnspan=1)
button_pokaz_kontakt.grid(row=2, column=1, columnspan=1)
button_usun_kontakt.grid(row=2, column=2, columnspan=1)
button_edytuj_kontakt.grid(row=2, column=3, columnspan=1)

# definicja obiektow ramki prawej
label_nowy_kontakt = Label(ramka_prawa, text="Nowy kontakt")

label_imie = Label(ramka_prawa, text="Imie:")
label_nazwisko = Label(ramka_prawa, text="Nazwisko:")
label_telefon = Label(ramka_prawa, text="Numer telefonu:")
label_email = Label(ramka_prawa, text="e-mail:")
label_dodaj_kontakt = Label(ramka_prawa, text="Dodaj kontakt")

entry_imie = Entry(ramka_prawa)
entry_nazwisko = Entry(ramka_prawa, width=30)
entry_telefon = Entry(ramka_prawa)
entry_email = Entry(ramka_prawa)
# entry_dodaj_kontakt = Button(ramka_prawa, text="Dodaj kontakt", command=lambda: test("hello"))
entry_dodaj_kontakt = Button(ramka_prawa, text="Dodaj kontakt", command=lambda: dodaj_kontakt(lista_kontaktow))

# ramka_prawa gridowanie
label_nowy_kontakt.grid(row=0, column=0, columnspan=3)

label_imie.grid(row=1, column=0, columnspan=1, sticky=W)
label_nazwisko.grid(row=2, column=0, columnspan=1, sticky=W)
label_telefon.grid(row=3, column=0, columnspan=1, sticky=W)
label_email.grid(row=4, column=0, columnspan=1, sticky=W)
label_dodaj_kontakt.grid(row=5, column=0, columnspan=1, sticky=W)

entry_imie.grid(row=1, column=1, columnspan=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, columnspan=1, sticky=W)
entry_telefon.grid(row=3, column=1, columnspan=1, sticky=W)
entry_email.grid(row=4, column=1, columnspan=1, sticky=W)
entry_dodaj_kontakt.grid(row=5, column=1, columnspan=1, sticky=W)

# definicja obiektow ramki dolnej
label_szczegoly_kontaktu = Label(ramka_dolna, text="Szczegoly kontaktu")

label_imie_output = Label(ramka_dolna, text="Imie:")
label_imie_output_wyswietl = Label(ramka_dolna, text="...", width=10)
label_nazwisko_output = Label(ramka_dolna, text="Nazwisko:")
label_nazwisko_output_wyswietl = Label(ramka_dolna, text="...", width=10)
label_telefon_output = Label(ramka_dolna, text="Numer telefonu:")
label_telefon_output_wyswietl = Label(ramka_dolna, text="...", width=10)
label_email_output = Label(ramka_dolna, text="e-mail:")
label_email_output_wyswietl = Label(ramka_dolna, text="...", width=10)

# ramka_dolna gridowanie
label_szczegoly_kontaktu.grid(row=0, column=0, columnspan=8, sticky=W)

label_imie_output.grid(row=1, column=0, columnspan=1, sticky=W)
label_imie_output_wyswietl.grid(row=1, column=1, columnspan=1, sticky=W)
label_nazwisko_output.grid(row=1, column=2, columnspan=1, sticky=W)
label_nazwisko_output_wyswietl.grid(row=1, column=3, columnspan=1, sticky=W)
label_telefon_output.grid(row=1, column=4, columnspan=1, sticky=W)
label_telefon_output_wyswietl.grid(row=1, column=5, columnspan=1, sticky=W)
label_email_output.grid(row=1, column=6, columnspan=1, sticky=W)
label_email_output_wyswietl.grid(row=1, column=7, columnspan=1, sticky=W)


# run app
root.mainloop()
