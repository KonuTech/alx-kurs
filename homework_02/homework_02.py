def homework_02_01() -> None:
    """
    Cwiczenie 71_2b
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
        :return:
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
        print(f"""The total amount to be paid is: {total_amount} PLN\nGood Bye!""")

    menu()
