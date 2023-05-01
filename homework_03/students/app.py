from typing import List

from homework_03.students.models.student import Student

tab = "\t"
new_line = "\n"
FILE_NAME = "dane.txt"
MODE = "r"
ENCODING = "utf-8"


def open_file(file_name, mode="r", encoding="utf-8"):
    return open(file=file_name, mode=mode, encoding=encoding)


def close_file(file_name):
    file_name.close()


def students():

    def add_student(file_name, mode="a", encoding=ENCODING):

        name = input(f"{tab}Input the Name of a Student:{new_line}")
        if not name:
            print(f"{tab}Error: Student's Name cannot be empty.{new_line}")
            return

        surname = input(f"{tab}Input the Surname of a Student:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        group = int(input(f"{tab}Input the Group ID of a Student:{new_line}"))
        if not group:
            print(f"{tab}Error: Student's Group cannot be empty.{new_line}")
            return

        pupil = Student(name=name.capitalize(), surname=surname.capitalize(), group=group)
        file = open_file(file_name, mode, encoding)
        file.write(f"{pupil.name},{pupil.surname},{pupil.group}\n")
        close_file(file)

        print(
            f"""
            {tab}Student {pupil.name}-{pupil.surname}-{pupil.group} added to the Students file.{new_line}
            """
        )

    def show_student(file_name, mode="r", delimiter=",", encoding=ENCODING):

        surname = input(f"Provide Student's Surname to be searched for.{new_line}")

        file = open_file(file_name, mode, encoding)
        rows = file.readlines()

        for r, row in enumerate(rows):
            if row.strip().split(delimiter)[1] == surname.capitalize():
                print(
                    f"""
                        Student {surname} found:
                    
                        ROW     :   {r}
                        NAME    :   {row.strip().split(delimiter)[0]}
                        SURNAME :   {row.strip().split(delimiter)[1]}
                        GROUP   :   {row.strip().split(delimiter)[2]}
                    """
                )

        close_file(file)

    def remove_student(file_name, delimiter=",", encoding="utf-8"):

        surname = input(f"Provide Student's Surname to be deleted.{new_line}")

        file = open_file(file_name, mode="r", encoding=encoding)
        rows = file.readlines()
        close_file(file)

        file = open_file(file_name, mode="w", encoding=encoding)
        for r, row in enumerate(rows):
            print(r, row)
            if row.strip().split(delimiter)[1] != surname.capitalize():
                file.write(
                    f"{row.strip().split(delimiter)[0]},{row.strip().split(delimiter)[1]},{row.strip().split(delimiter)[2]}{new_line}"
                )

        close_file(file)

        print(f"Student {surname} deleted.")

    def edit_student(file_name, delimiter=",", encoding="utf-8"):

        surname = input(f"Editing a Student data. Provide Student's Surname to be searched for.{new_line}")

        file = open_file(file_name, mode="r", encoding=encoding)
        rows = file.readlines()
        close_file(file)

        file = open_file(file_name, mode="w", encoding=encoding)
        for r, row in enumerate(rows):
            if row.strip().split(delimiter)[1] != surname.capitalize():
                file.write(
                    f"{row.strip().split(delimiter)[0]},{row.strip().split(delimiter)[1]},{row.strip().split(delimiter)[2]}{new_line}"
                )

        close_file(file)

        name = input(f"{tab}Input the Name of a Student:{new_line}")
        if not name:
            print(f"{tab}Error: Student's Name cannot be empty.{new_line}")
            return

        surname = input(f"{tab}Input the Surname of a Student:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        group = int(input(f"{tab}Input the Group ID of a Student:{new_line}"))
        if not group:
            print(f"{tab}Error: Student's Group cannot be empty.{new_line}")
            return

        pupil = Student(name=name.capitalize(), surname=surname.capitalize(), group=group)

        file = open_file(file_name, mode="a", encoding=ENCODING)
        file.write(f"{pupil.name},{pupil.surname},{pupil.group}\n")
        close_file(file)

        print(
            f"""
            {tab}Student {surname} edited.{new_line}
            New data:{new_line}{pupil.name}-{pupil.surname}-{pupil.group} added to the Students file.{new_line}
            """
        )

    menu_prompt = f"""
            Cwiczenie 85:
    
            A - Add a Student
            S - Show a Student
            D - Delete a Student
            E - Edit a Student
            Q - Exit
    
            Enter your choice:{new_line}
            """

    menu_options = {
        "a": add_student,
        "s": show_student,
        "d": remove_student,
        "e": edit_student
    }

    def menu() -> None:
        """
        :return: None
        """

        while (selection := input(menu_prompt)) != "q":
            if selection == "a":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "s":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "d":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "e":
                menu_options[selection](file_name=FILE_NAME)
            else:
                print("Invalid input selected. Please try again.")

    menu()
