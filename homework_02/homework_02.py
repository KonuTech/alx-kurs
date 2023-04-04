def homework_02_01():
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

    def menu():
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

        def add_product():
            key = input("Add a name of a product to be added\n")
            value = input("Specify the price for added product\n")
            products.update({f"{key}": int(value)})

        def view_products():
            tab = '\t'
            print("Current products\nin your basket are:")
            for k, v in products.items():
                print(f"{3 * tab}{k}:{tab}{v}")

        menu_options = {
            "1": add_product,
            "2": view_products
        }

        while (selection := input(menu_prompt)) != "3":
            try:
                if selection == "1":
                    menu_options[selection]()
                    print("Product added.")
                if selection == "2":
                    menu_options[selection]()
                    print("Products listed.")
                else:
                    print("Please, use only: 1, 2 or 3 as inputs.")
            except KeyError:
                print("Invalid input selected. Please try again.")

        for product, price in products.items():
            total_amount += price
        print(f"""The total amount to be paid is: {total_amount} PLN\nGood Bye!""")

    menu()
