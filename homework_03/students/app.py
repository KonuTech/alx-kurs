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
    students = []

    def add_student(students: List[Student], file_name=FILE_NAME, mode="a", encoding=ENCODING):

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

        for s, student in enumerate(students):
            if student.surname == pupil.surname:
                print(f"{tab}Error: Student's Surname already in a list of Students.{new_line}")
                return

        students.append(pupil)
        print(
            f"""
            {tab}Student {pupil.name}-{pupil.surname}-{pupil.group} added to the Students file.{new_line}
            """
        )

        file = open_file(file_name, mode, encoding)
        file.write(f"{pupil.name},{pupil.surname},{pupil.group}\n")
        close_file(file)

    def show_student(file_name=FILE_NAME, mode="r", delimiter=",", encoding=ENCODING):

        surname = input(f"Provide Student's Surname to search for.{new_line}")

        file = open_file(file_name, mode, encoding)
        rows = file.readlines()

        for r, row in enumerate(rows):
            print(r, row)
            if row.strip().split(delimiter)[1] == surname.capitalize():
                print(
                    f"""
                        ROW     :   {r}
                        NAME    :   {row.strip().split(delimiter)[0]}
                        SURNAME :   {row.strip().split(delimiter)[1]}
                        GROUP   :   {row.strip().split(delimiter)[2]}
                    """
                )

        close_file(file)

    def remove_student(students: List[Student]):
        pass

    def edit_student(students: List[Student]):
        pass

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
                menu_options[selection](students)
            elif selection == "s":
                menu_options[selection]()
            elif selection == "d":
                menu_options[selection](students)
            elif selection == "e":
                menu_options[selection](students)
            else:
                print("Invalid input selected. Please try again.")

    menu()
