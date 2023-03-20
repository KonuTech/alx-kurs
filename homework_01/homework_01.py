def homework_01_01(zm1: str, zm2: str, zm3: str, zm4: str, zm5: str, zm6: str, zm7: str, zm8: str, zm9: str) -> None:
    """
    Printing homework 01.01
    :param zm1:
    :param zm2:
    :param zm3:
    :param zm4:
    :param zm5:
    :param zm6:
    :param zm7:
    :param zm8:
    :param zm9:
    :return: None
    """
    print(f"{zm6} {zm8} {zm7} {zm1} {zm3} {zm9} {zm5} {zm4} {zm2}")


def homework_01_02(imie: str, nazwisko: str, wiek: int, pensja: float, stanowisko: str) -> None:
    """
    Printing homework 01.02
    :param imie:
    :param nazwisko:
    :param wiek:
    :param pensja:
    :param stanowisko:
    :return: None
    """
    print(f"{imie} {nazwisko} {wiek} {pensja} {stanowisko}")


def homework_01_03() -> None:
    """
    Printing homework 01.03
    :return: None
    """

    menu_prompt = """
            -- Menu --

        1) Choose a printer type
        2) How much time do you have?
        3) How many pages you want to print?
        4) Start printing and exit

        Enter your choice: 
    """

    def get_printer_type() -> int:
        """
        :return:
        """
        while True:
            printer_type = input(
                """
                    What type of printer you use?
                    Valid values:
                    For black and white printer press: 0
                    For color printer press: 1
                """
            )

            if printer_type == str(0):
                print("You have chosen black and white printer. Continue with next step.")
                return 0
            if printer_type == str(1):
                print("You have chosen color printer. Continue with next step.")
                return 1
            else:
                print("Wrong input. Try again.")

    def get_max_time() -> float:
        """
        :return:
        """
        while True:
            available_time = input(
                """
                    How much time in minutes do you have for printing?
                    Valid values: integers and dot delimited floats
                """
            )

            if len(available_time) != 0:
                print(f"You have {available_time} minutes available for printing.\n")
                return float(available_time)
            else:
                print("Missing input. Try again.")

    def get_number_of_pages() -> int:
        """
        :return:
        """
        while True:
            pages_number = input(
                """
                    How much pages you want to print?
                    Valid values: integers
                """
            )

            if (len(pages_number) != 0 and int(pages_number)) > 0:
                print(f"You want to print {pages_number} pages.\n")
                return int(pages_number)
            else:
                print("Wrong input. Try again.")

    MENU_OPTIONS = {
        "1": get_printer_type,
        "2": get_max_time,
        "3": get_number_of_pages
    }

    def menu():
        """
        :return:
        """
        data = {
            "printer_type": 0,
            "available_time": 0,
            "number_of_pages": 0
        }
        while (selection := input(menu_prompt)) != "4":
            try:
                if selection == "1":
                    printer_type = MENU_OPTIONS[selection]()
                    data.update({"printer_type": printer_type})
                if selection == "2":
                    available_time = MENU_OPTIONS[selection]()
                    data.update({"available_time": available_time})
                if selection == "3":
                    number_of_pages = MENU_OPTIONS[selection]()
                    data.update({"number_of_pages": number_of_pages})
            except KeyError:
                print("Invalid input selected. Please try again.")
            print(
                f"""
                    My current setup: {data}
                """
            )
        if data['printer_type'] == 1:
            print(
                f"""
                    Printing a following total number of pages in color:
                    {int(data['available_time'] / 5 * 2)}
                """
            )
            data.update({"number_of_pages": data['available_time'] / 5 * 2})
            print(data)
        else:
            print(
                f"""
                    Printing a following total number of pages in black and white:
                    {int(data['available_time'] / 2 * 8)}
                """
            )
            data.update({"number_of_pages": data['available_time'] / 2 * 8})
            print(data)

    menu()


def homework_01_04() -> float:
    """
    Printing homework 01.04
    :return: float
    """
    list_1 = []
    list_2 = []

    while len(list_1) < 3:
        list_1.append(float(input("Add a number to list_1\n")))

    while len(list_2) < 3:
        list_2.append(float(input("Add a number to list_2\n")))

    print(f"Summing all following numbers: {list_1} {list_2} ")

    print(f"A sum: {sum(list_1) + sum(list_2)}")
