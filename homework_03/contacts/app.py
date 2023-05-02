import pickle

from homework_03.contacts.models.contact import Contact

tab = "\t"
new_line = "\n"
FILE_NAME = "people.dat"
MODE = "wb"
ENCODING = "utf-8"
DELIMITER = ";"

notes = []


def open_file(file_name=FILE_NAME, mode=MODE):
    return open(file_name, mode)


def close_file(file_name=FILE_NAME):
    file_name.close()


def contacts():
    def show_contact(file_name, mode="rb", delimiter=DELIMITER, encoding=ENCODING):

        if len(notes) == 0:
            print(f"{tab}Empty list of Contacts. Please register a Contact first.{new_line}")
            return

        contact_surname = input("\tInput a Surname of a Contact to be listed:\n")
        if not contact_surname:
            print("\tMissing Contact's Surname. Please pass a Contact's Surname.\n")
            return

        for n, note in enumerate(notes):
            if note.surname == contact_surname.capitalize():
                print(
                    f"""
                    Contact details:
                        ID: {n + 1}
                        NAME: {note.name}
                        SURNAME: {note.surname}
                        PHONES: {note.phones}
                        EMAILS: {note.emails}
                    """
                )

    def add_contact(file_name, mode="r", delimiter=DELIMITER, encoding=ENCODING):

        name = input(f"{tab}Input the Name of a Contact:{new_line}")
        if not name:
            print(f"{tab}Error: Contact's Name cannot be empty.{new_line}")
            return

        surname = input(f"{tab}Input a Surname of a Contact:{new_line}")
        if not surname:
            print(f"{tab}Error: Contact's Surname cannot be empty.{new_line}")
            return

        phone = input(f"{tab}Input a Phone Number of a Contact:{new_line}")
        if not phone:
            print(f"{tab}Error: Contact's Phone Number cannot be empty.{new_line}")
            return

        email = input(f"{tab}Input an E-mail of a Contact:{new_line}")
        if not email:
            print(f"{tab}Error: Contact's E-mail cannot be empty.{new_line}")
            return

        person = Contact(
            name=name.capitalize(),
            surname=surname.capitalize(),
            phones=[phone],
            emails=[email]
        )

        for n, note in enumerate(notes):
            if note.surname == person.surname:
                print(f"{tab}Error: Contact Surname already in a list of Contacts.{new_line}")
                return

        notes.append(person)
        print(
            f"""
            {tab}Contact {person.name}-{person.surname}-{person.phones}-{person.emails} added to the Clinics list.{new_line}
            """
        )

        f = open_file(file_name=file_name, mode='wb')
        pickle.dump(person, f)
        close_file(f)

    def remove_contact(file_name, delimiter=DELIMITER, encoding=ENCODING):
        """
        Prompts the user to provide a Surname of a Contact to be removed.
        :return: None
        """
        if len(notes) == 0:
            print(f"{tab}Empty list of Contacts. Please register a Contact first.{new_line}")
            return

        contact_surname = input("\tInput a Surname of a Contact to be listed:\n")
        if not contact_surname:
            print("\tMissing Contact's Surname. Please pass a Contact's Surname.\n")
            return

        for n, note in enumerate(notes):
            if note.surname == contact_surname.capitalize():
                notes.pop(n)
                print(f"{tab}Contact {note.surname} removed from the list of registered Contacts.{new_line}")
                print(
                    f"""
                    Contact {note.surname} removed:
                        ID: {n + 1}
                        NAME: {note.name}
                        PHONES: {note.phones}
                        EMAILS: {note.emails}
                    """
                )

    def add_phone(file_name, delimiter=DELIMITER, encoding=ENCODING):

        contact_surname = input(f"{tab}Input a Surname of a Contact:{new_line}")
        if not contact_surname:
            print(f"{tab}Error: Contact's Surname cannot be empty.{new_line}")
            return

        phone = input(f"{tab}Input a Phone number of a Contact:{new_line}")
        if not phone:
            print(f"{tab}Error: Contact's Phone number cannot be empty.{new_line}")
            return

        for n, note in enumerate(notes):
            if note.surname == contact_surname.capitalize():
                person = Contact(
                    name=note.name,
                    surname=note.surname,
                    phones=note.phones,
                    emails=note.emails
                )

                person.phones.append(phone)

    def remove_phone(file_name, delimiter=DELIMITER, encoding=ENCODING):

        contact_surname = input(f"{tab}Input a Surname of a Contact:{new_line}")
        if not contact_surname:
            print(f"{tab}Error: Contact's Surname cannot be empty.{new_line}")
            return

        contact_phone = input(f"{tab}Input a Phone number of a Contact to be removed:{new_line}")
        if not contact_phone:
            print(f"{tab}Error: Contact's Phone number to be removed cannot be empty.{new_line}")
            return

        for n, note in enumerate(notes):
            if note.surname == contact_surname.capitalize():
                for p, phone in enumerate(note.phones):
                    if phone == contact_phone:
                        note.phones.remove(contact_phone)

    def add_email(file_name, delimiter=DELIMITER, encoding=ENCODING):

        contact_surname = input(f"{tab}Input a Surname of a Contact:{new_line}")
        if not contact_surname:
            print(f"{tab}Error: Contact's Surname cannot be empty.{new_line}")
            return

        email = input(f"{tab}Input an E-mail address of a Contact:{new_line}")
        if not email:
            print(f"{tab}Error: Contact's E-mail address cannot be empty.{new_line}")
            return

        for n, note in enumerate(notes):
            if note.surname == contact_surname.capitalize():
                pupil = Contact(
                    name=note.name,
                    surname=note.surname,
                    phones=note.phones,
                    emails=note.emails
                )

                pupil.emails.append(email)

    def remove_email(file_name, delimiter=DELIMITER, encoding=ENCODING):

        contact_surname = input(f"{tab}Input the Surname of a Contact:{new_line}")
        if not contact_surname:
            print(f"{tab}Error: Contact's Surname cannot be empty.{new_line}")
            return

        contact_email = input(f"{tab}Input an E-mail address of a Contact to be removed:{new_line}")
        if not contact_email:
            print(f"{tab}Error: Contact's E-mail address to be removed cannot be empty.{new_line}")
            return

        for n, note in enumerate(notes):
            if note.surname == contact_surname.capitalize():
                for e, email in enumerate(note.emails):
                    if email == contact_email:
                        note.emails.remove(contact_email)

    menu_prompt = f"""
            Cwiczenie 85:

            1 - Show a Contact
            2 - Add a Contact
            3 - Remove a Contact
            4 - Add a Phone number
            5 - Remove a Phone number
            6 - Add an e-mail address 
            7 - Remove an e-mail address
            8 - Exit

            Enter your choice:{new_line}
            """

    menu_options = {
        "1": show_contact,
        "2": add_contact,
        "3": remove_contact,
        "4": add_phone,
        "5": remove_phone,
        "6": add_email,
        "7": remove_email
    }

    def menu() -> None:
        """
        :return: None
        """

        while (selection := input(menu_prompt)) != "8":
            if selection == "1":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "2":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "3":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "4":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "5":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "6":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "7":
                menu_options[selection](file_name=FILE_NAME)
            else:
                print("Invalid input selected. Please try again.")

    menu()
