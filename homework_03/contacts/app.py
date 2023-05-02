from homework_03.contacts.models.contact import Contact

tab = "\t"
new_line = "\n"
FILE_NAME = "dane.txt"
MODE = "r"
ENCODING = "utf-8"
DELIMITER = ";"


def open_file(file_name, mode="r", encoding=ENCODING):
    return open(file=file_name, mode=mode, encoding=encoding)


def close_file(file_name):
    file_name.close()


def contacts():
    def show_contact(file_name, mode="a", delimiter=DELIMITER, encoding=ENCODING):
        pass

    def add_contact(file_name, mode="r", delimiter=DELIMITER, encoding=ENCODING):
        pass

    def remove_contact(file_name, delimiter=DELIMITER, encoding=ENCODING):
        pass

    def add_phone(file_name, delimiter=DELIMITER, encoding=ENCODING):
        pass

    def remove_phone(file_name, delimiter=DELIMITER, encoding=ENCODING):
        pass

    def add_email(file_name, delimiter=DELIMITER, encoding=ENCODING):
        pass

    def remove_email(file_name, delimiter=DELIMITER, encoding=ENCODING):
        pass

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
