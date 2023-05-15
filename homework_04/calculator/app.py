from tkinter import *


# def homework_02_09() -> bool:
#     """
#     Cwiczenie 67-4
#     :return: None
#     """
#     print("Cwiczenie 67-4\n")
#
#     while True:
#
#         while True:
#             try:
#                 number_1 = float(input(
#                     f"""
#                         Enter first number.
#                         Valid numbers: floats
#                     """
#                 ))
#                 break
#             except ValueError:
#                 print("Enter floats or integers. Please try again")
#
#         while True:
#             try:
#                 operator = input(
#                     f"""
#                         Enter mathematical opertor.
#                         Valid operators are: + - / *
#                     """
#                 )
#                 assert operator in ("+", "-", "/", "*")
#                 break
#             except AssertionError:
#                 print("Wrong operator. Please try again.")
#
#         while True:
#             try:
#                 number_2 = float(input(
#                     f"""
#                         Enter second number.
#                         Valid numbers: floats
#                     """
#                 ))
#                 break
#             except ValueError:
#                 print("Enter floats or integers. Please try again")
#
#         if operator == "+":
#             result = number_1 + number_2
#             print(
#                 f"""
#                     Calculation: {number_1} {operator} {number_2}
#                     Result: {result}
#                 """
#             )
#
#         if operator == "-":
#             result = number_1 - number_2
#             print(
#                 f"""
#                     Calculation: {number_1} {operator} {number_2}
#                     Result: {result}
#                 """
#             )
#
#         if operator == "/":
#             result = number_1 / number_2
#             print(
#                 f"""
#                     Calculation: {number_1} {operator} {number_2}
#                     Result: {result}
#                 """
#             )
#
#         if operator == "*":
#             result = number_1 * number_2
#             print(
#                 f"""
#                     Calculation: {number_1} {operator} {number_2}
#                     Result: {result}
#                 """
#             )
#
#         return False


root = Tk()
root.geometry("250x350")
root.title("Calculator")

calculation = StringVar()
result = StringVar()

# frame upper
frame_upper = Frame(root)
frame_upper.grid(row=0, column=0, pady=(20, 20), padx=20, sticky="NSE")

# frame upper label
frame_upper_label = Label(frame_upper, textvariable=calculation)
frame_upper_label.grid(row=0, column=0, columnspan=3, sticky="NSEW")
calculation.set("2 + 2")

# frame middle
frame_middle = Frame(root)
frame_middle.grid(row=1, column=0, pady=(20, 20), padx=20, sticky="NSE")

# frame middle label
frame_middle_label = Label(frame_middle, textvariable=result)
frame_middle_label.grid(row=0, column=0, columnspan=3, sticky="NSEW")
result.set("4")

# frame bottom
frame_bottom = Frame(root)
frame_bottom.grid(row=2, column=0, pady=(20, 20), padx=20, sticky="NSEW")

# buttton one
button_one = Button(frame_bottom, text="1", width=5, height=2)
button_one.grid(row=2, column=0, columnspan=1, sticky="NSEW")

# buttton two
button_two = Button(frame_bottom, text="2", width=5, height=2)
button_two.grid(row=2, column=1, columnspan=1, sticky="NSEW")

# buttton three
button_three = Button(frame_bottom, text="3", width=5, height=2)
button_three.grid(row=2, column=2, columnspan=1, sticky="NSEW")

# buttton four
button_four = Button(frame_bottom, text="4", width=5, height=2)
button_four.grid(row=1, column=0, columnspan=1, sticky="NSEW")

# buttton five
button_five = Button(frame_bottom, text="5", width=5, height=2)
button_five.grid(row=1, column=1, columnspan=1, sticky="NSEW")

# buttton six
button_six = Button(frame_bottom, text="6", width=5, height=2)
button_six.grid(row=1, column=2, columnspan=1, sticky="NSEW")

# buttton seven
button_seven = Button(frame_bottom, text="7", width=5, height=2)
button_seven.grid(row=0, column=0, columnspan=1, sticky="NSEW")

# buttton eight
button_eight = Button(frame_bottom, text="8", width=5, height=2)
button_eight.grid(row=0, column=1, columnspan=1, sticky="NSEW")

# buttton nine
button_nine = Button(frame_bottom, text="9", width=5, height=2)
button_nine.grid(row=0, column=2, columnspan=1, sticky="NSEW")

# buttton zero
button_zero = Button(frame_bottom, text="0", width=5, height=2)
button_zero.grid(row=3, column=0, columnspan=1)

# buttton equality
button_equality = Button(frame_bottom, text="=")
button_equality.grid(row=3, column=1, columnspan=2, sticky="NSEW")

# buttton muliply
button_muliply = Button(frame_bottom, text="*", width=5, height=2)
button_muliply.grid(row=0, column=4, columnspan=1)

# buttton substraction
button_substraction = Button(frame_bottom, text="-", width=5, height=2)
button_substraction.grid(row=1, column=4, columnspan=1)

# buttton addition
button_addition = Button(frame_bottom, text="+", width=5, height=2)
button_addition.grid(row=2, column=4, columnspan=1)

# buttton clear
button_clear = Button(frame_bottom, text="R", width=5, height=2)
button_clear.grid(row=3, column=4, columnspan=1)


# run app
root.mainloop()