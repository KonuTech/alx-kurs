from homework_02.functions.functions import *


def homework_02_01() -> None:
    """
    Cwiczenie 71_2b
    :return: None
    """
    menu_prompt = """
        Cwiczenie 71_2b:
        
                   -- Shop Menu --
            1) Add a product to the basket
            2) View content of your basket
            3) Exit
            
            Enter your choice:\n
        """

    def menu() -> None:
        """
        :return: None
        """
        total_amount = 0

        products = {
            "bread": 3.50,
            "juice": 6.00,
            "water": 1.80,
            "sugar": 4.25
        }

        def add_product() -> None:
            key = input("Add a name of a product to be added\n")
            try:
                value = float(input("Specify the price for added product\n"))
                products.update({f"{key}": value})
                print("Product added.")
            except ValueError:
                print("Expected float numbers as inputs for prices. Please try again.")

        def view_products() -> None:
            tab = '\t'
            print("Current products\nin your basket are:")
            for k, v in products.items():
                print(f"{3 * tab}{k}:{tab}{v}\n")
            print("Products listed.")

        menu_options = {
            "1": add_product,
            "2": view_products
        }

        while (selection := input(menu_prompt)) != "3":
            try:
                if selection == "1":
                    menu_options[selection]()
                if selection == "2":
                    menu_options[selection]()
            except KeyError:
                print("Invalid input selected. Please try again.")

        for product, price in products.items():
            total_amount += price
        print(f"""The total amount to be paid is: {total_amount} PLN\nGood Bye!\n""")

    menu()


def homework_02_02() -> None:
    """
    Cwiczenie 61
    :return: None
    """
    print("Cwiczenie 61:\n")

    result = []
    value = int(input("Provide an integer:\n"))

    print(f"Provided integer:\n{value}")

    try:
        for i in range(0, value):
            if i % 2 != 0:
                result.append(str(i))
    except ValueError:
        print("Invalid input.")
    finally:
        print(f"{' '.join(result)}\n")


def homework_02_03(minimum: int, maximum: int, steps: int) -> None:
    """
    Cwiczenie 46-4
    :param minimum: int
    :param maximum: int
    :param steps: int
    :return: None
    """
    print("Cwiczenie 46-4:\n")

    doubles = []
    doubles_indexes = []
    doubles_count = 0

    values = get_values(minimum, maximum, steps)

    for i in range(len(values)):
        for k in range(i+1, len(values)):
            if values[i] == values[k]:
                doubles.append(values[i])
                doubles_indexes.append(i)
                doubles_count += 1

    print(
        f"""
        Values                  : {values}
        Doubles                 : {set(doubles)}
        Doubles indexes         : {set(doubles_indexes)}
        Doubles count           : {doubles_count}
        """""
    )

    results = remove_item(values, doubles)

    print(
        f"""
        Non-duplicate values    : {results}\n
        """
    )


def homework_02_04(minimum: int, maximum: int, steps: int) -> bool:
    """
    Cwiczenie 62-2
    :param minimum: int
    :param maximum: int
    :param steps: int
    :return: None
    """
    print("Cwiczenie 62-2:\n")

    values = get_values(minimum, maximum, steps)
    print(values)

    while True:
        value = input("Provide an integer between 1 and 25. Provide 0 to quit.\n")
        print(f"Provided integer:\n{value}")

        while True:
            if value != "0":
                try:
                    assert int(value) in set(values)
                    print(f"Integer {value} found.\n")
                    break
                except AssertionError:
                    print(f"Integer {value} NOT found. Please try again.\n")
                    break
                except ValueError:
                    print(f"Provide an integer. Try again.\n")
                    break
            else:
                return False


def homework_02_05(minimum: int, maximum: int, steps: int) -> bool:
    """
    Cwiczenie 59_2
    :param minimum: int
    :param maximum: int
    :param steps: int
    :return: None
    """
    print("Cwiczenie 59_2:\n")
    count = 1

    while True:
        if count < 6:
            try:
                values = get_values(minimum, maximum, steps)
                result = int(input(
                    f"""
                    How much is it: {values[0]} * {values[1]} ?\n
                    """
                ))
                if result == values[0] * values[1]:
                    count += 1
                    print("Correct anwer.\n")
                else:
                    print("Wrong answer.\n")
            except ValueError:
                print("Provide an integer. Please try again.\n")
        else:
            return False


def homework_02_06(word: str) -> None:
    """
    Cwiczenie 26-10
    :param word: str
    :return: None
    """
    print("Cwiczenie 26-10:\n")

    dictionary = {}

    for c in word:
        if c not in dictionary.keys():
            dictionary.update({c: 1})
        else:
            dictionary[c] = dictionary[c] + 1

    for k, v in dictionary.items():
        print(f"Liter {k} jest: {v}")


def homework_02_07(values: list):
    """
    Cwiczenie 62-4
    :param values:
    :return: None
    """
    print("Cwiczenie 62-4\n")

    minimal_index = 1

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[j] < values[minimal_index]:
                minimal_index = j

        values[i], values[minimal_index] = values[minimal_index], values[i]

    print(values)


def homework_02_08(kina: list, filmy: dict, cena_bilet: float) -> bool:
    """
    Cwiczenie 26-10
    :param kina: list
    :param filmy: dict
    :param cena_bilet: float
    :return: None
    """
    print("Cwiczenie 26-10\n")

    litery = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x",
              "c", "v", "b", "n", "m"]

    while True:

        print(
            f"""
                Lista kin:
                {", ".join(kina)}
            """
        )

        while True:
            try:
                id_kino = int(input("Podaj ID kina\n"))
                print(
                    f"""
                        Wybrane kino:
                        {kina[id_kino - 1]}
                    """
                )
                break
            except ValueError:
                print("PODAJ LICZBE CALKOWITA")
            except IndexError:
                print("NIEWLASCIWY INDEX WYBRANEGO KINA")

        print(
            f"""
                Lista filmow do wyboru:
                {", ".join(filmy[id_kino - 1])}
            """
        )

        while True:
            try:
                id_filmu = int(input("Podaj ID filmu\n"))
                print(
                    f"""
                        Wybrany film:
                        {filmy[id_kino - 1][id_filmu - 1]}
                    """
                )
                break
            except ValueError:
                print("PODAJ LICZBE CALKOWITA")
            except IndexError:
                print("NIEWLASCIWY INDEX WYBRANEGO KINA")

        while True:
            try:
                liczba_osob = int(input("Podaj liczbe osob\n"))
                print(
                    f"""
                        Podana liczba osob:
                        {liczba_osob}
                    """
                )
                break
            except ValueError:
                print("PODAJ LICZBE CALKOWITA")

        imie_zamawiajacego = input("Podaj swoje imie\n")

        for i in range(len(imie_zamawiajacego)):
            try:
                assert imie_zamawiajacego[i] in set(litery)
            except AssertionError:
                print("Niepoprawny znak")

        print(
            f"""
                Kino: {kina[id_kino - 1]}
                Film: {filmy[id_kino - 1][id_filmu - 1]}
                Liczba osob: {liczba_osob}
                Imie osoby rezerwujacej: {imie_zamawiajacego.capitalize()}
                RAZEM DO ZAPLATY: {liczba_osob} * {cena_bilet} PLN = {liczba_osob * cena_bilet} PLN
            """
        )

        return False


def homework_02_09() -> bool:
    """
    Cwiczenie 67-4
    :return: None
    """
    print("Cwiczenie 67-4\n")

    while True:

        while True:
            try:
                number_1 = float(input(
                    f"""
                        Enter first number.
                        Valid numbers: floats
                    """
                ))
                break
            except ValueError:
                print("Enter floats or integers. Please try again")

        while True:
            try:
                operator = input(
                    f"""
                        Enter mathematical opertor.
                        Valid operators are: + - / *
                    """
                )
                assert operator in ("+", "-", "/", "*")
                break
            except AssertionError:
                print("Wrong operator. Please try again.")

        while True:
            try:
                number_2 = float(input(
                    f"""
                        Enter second number.
                        Valid numbers: floats
                    """
                ))
                break
            except ValueError:
                print("Enter floats or integers. Please try again")

        if operator == "+":
            result = number_1 + number_2
            print(
                f"""
                    Calculation: {number_1} {operator} {number_2}
                    Result: {result}
                """
            )

        if operator == "-":
            result = number_1 - number_2
            print(
                f"""
                    Calculation: {number_1} {operator} {number_2}
                    Result: {result}
                """
            )

        if operator == "/":
            result = number_1 / number_2
            print(
                f"""
                    Calculation: {number_1} {operator} {number_2}
                    Result: {result}
                """
            )

        if operator == "*":
            result = number_1 * number_2
            print(
                f"""
                    Calculation: {number_1} {operator} {number_2}
                    Result: {result}
                """
            )

        return False
