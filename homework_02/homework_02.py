import random


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


def homework_02_03() -> None:
    """
    Cwiczenie 46-4
    :return: None
    """
    print("Cwiczenie 46-4:\n")

    values = []
    dubles = []
    dubles_count = 0
    dubles_indexes = []
    result = []

    for i in range(0, 10):
        values.append(random.randint(1, 10))

    values_shorter = values.copy()
    print(values)
    print(values_shorter)

    for i in range(len(values)):
        # values_shorter.pop(i)
        for k in range(i+1, len(values_shorter)):
            # print("values[i]:", values[i], "values[k]:", values[k])
            if values[i] == values[k]:
                print("values[i]:", values[i], "values[k]:", values[k])
                dubles.append(values[i])
                dubles_indexes.append(i)
                dubles_count += 1
                # values_shorter.pop(i)

    for j in range(len(set(dubles_indexes))):
        print("indexes[j]:", dubles_indexes[j])
        # values.pop(indexes(j))


    print("values:", values)
    print("dubles:", set(dubles))
    print("dubles_indexes:", set(dubles_indexes))
    print("dubles_count:", dubles_count)
    print(values_shorter)
