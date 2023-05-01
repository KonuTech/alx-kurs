from homework_03.students.models.student import Student

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


def students():
    def add_student(file_name, mode="a", delimiter=DELIMITER, encoding=ENCODING):

        name = input(f"{tab}Input the Name of a Student:{new_line}")
        if not name:
            print(f"{tab}Error: Student's Name cannot be empty.{new_line}")
            return

        surname = input(f"{tab}Input the Surname of a Student:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        group = input(f"{tab}Input the Group ID of a Student:{new_line}")
        if not group:
            print(f"{tab}Error: Student's Group cannot be empty.{new_line}")
            return

        pupil = Student(
            name=name.capitalize(),
            surname=surname.capitalize(),
            group=group,
            grades=[]
        )

        file = open_file(file_name, mode, encoding)
        file.write(f"{pupil.name}{delimiter}{pupil.surname}{delimiter}{pupil.group}{delimiter}{pupil.grades}{new_line}")
        close_file(file)

        print(
            f"""
            {tab}Student {pupil.name}-{pupil.surname}-{pupil.group}-{pupil.grades} added to the Students file.{new_line}
            """
        )

    def show_student(file_name, mode="r", delimiter=DELIMITER, encoding=ENCODING):

        name = input(f"{tab}Input the Name of a Student:{new_line}")
        surname = input(f"{tab}Provide Student's Surname to be searched for.{new_line}")

        file = open_file(file_name, mode, encoding)
        rows = file.readlines()

        for r, row in enumerate(rows):
            if row.strip().split(delimiter)[1] == surname.capitalize():
                if row.strip().split(delimiter)[0] == name.capitalize():
                    print(
                        f"""
                            Student {surname} found:
                        
                            ROW     :   {r}
                            NAME    :   {row.strip().split(delimiter)[0]}
                            SURNAME :   {row.strip().split(delimiter)[1]}
                            GROUP   :   {row.strip().split(delimiter)[2]}
                            GRADES  :   {row.strip().split(delimiter)[3]}
                        """
                    )
        print(f"{tab}Student {name.capitalize()} {surname.capitalize()} not found. Please try again.{new_line}")
        close_file(file)

    def remove_student(file_name, delimiter=DELIMITER, encoding=ENCODING):

        surname = input(f"{tab}Provide Student's Surname to be deleted.{new_line}")

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

        print(f"{tab}Student {surname} deleted.")

    def edit_student(file_name, delimiter=DELIMITER, encoding=ENCODING):

        surname = input(f"{tab}Editing a Student data. Provide Student's Surname to be searched for.{new_line}")

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

        group = input(f"{tab}Input the Group ID of a Student:{new_line}")
        if not group:
            print(f"{tab}Error: Student's Group cannot be empty.{new_line}")
            return

        pupil = Student(
            name=name.capitalize(),
            surname=surname.capitalize(),
            group=group,
            grades=[]
        )

        file = open_file(file_name, mode="a", encoding=ENCODING)
        file.write(f"{pupil.name}{delimiter}{pupil.surname}{delimiter}{pupil.group}{delimiter}{pupil.grades}{new_line}")
        close_file(file)

        print(
            f"""
            {tab}Student {surname} edited.{new_line}
            {tab}New data:{new_line}{pupil.name}-{pupil.surname}-{pupil.group}-{pupil.grades} added to the Students file.{new_line}
            """
        )

    def add_grade(file_name, delimiter=DELIMITER, encoding=ENCODING):

        surname = input(f"{tab}Input the Surname of a Student:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        grade = input(f"{tab}Input the Grade of a Student:{new_line}")
        if not grade:
            print(f"{tab}Error: Student's Grade cannot be empty.{new_line}")
            return

        file = open_file(file_name, mode="r", encoding=encoding)
        rows = file.readlines()
        close_file(file)

        file = open_file(file_name, mode="w", encoding=encoding)
        for r, row in enumerate(rows):
            if row.strip().split(delimiter)[1] != surname.capitalize():
                file.write(
                    f"{row.strip().split(delimiter)[0]},{row.strip().split(delimiter)[1]},{row.strip().split(delimiter)[2]},{row.strip().split(delimiter)[3]}{new_line}"
                )
            elif row.strip().split(delimiter)[1] == surname.capitalize():
                pupil = Student(
                    name=row.strip().split(delimiter)[0],
                    surname=row.strip().split(delimiter)[1],
                    group=row.strip().split(delimiter)[2],
                    grades=eval(row.strip().split(delimiter)[3])
                )

                pupil.grades.append(grade)

                file = open_file(file_name, mode="a", encoding=ENCODING)
                file.write(
                    f"{pupil.name}{delimiter}{pupil.surname}{delimiter}{pupil.group}{delimiter}{pupil.grades}{new_line}"
                )

        close_file(file)

    def get_mean(file_name, delimiter=DELIMITER, encoding=ENCODING):

        surname = input(f"{tab}Input the Surname of a Student:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        file = open_file(file_name, mode="r", encoding=encoding)
        rows = file.readlines()
        close_file(file)

        for r, row in enumerate(rows):
            if row.strip().split(delimiter)[1] == surname.capitalize():
                pupil = Student(
                    name=row.strip().split(delimiter)[0],
                    surname=row.strip().split(delimiter)[1],
                    group=row.strip().split(delimiter)[2],
                    grades=eval(row.strip().split(delimiter)[3])
                )

                print(f"""{tab}Student {pupil.surname} got an Average of{new_line}{pupil.get_average()}{new_line}""")

    menu_prompt = f"""
            Cwiczenie 85:
    
            A - Add a Student
            S - Show a Student
            D - Delete a Student
            E - Edit a Student
            G - Add a Grade to the Student
            M - Get a Mean of Student's Grades 
            Q - Exit
    
            Enter your choice:{new_line}
            """

    menu_options = {
        "a": add_student,
        "s": show_student,
        "d": remove_student,
        "e": edit_student,
        "g": add_grade,
        "m": get_mean
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
            elif selection == "g":
                menu_options[selection](file_name=FILE_NAME)
            elif selection == "m":
                menu_options[selection](file_name=FILE_NAME)
            else:
                print("Invalid input selected. Please try again.")

    menu()
