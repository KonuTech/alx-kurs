from tkinter import *


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