from homework_03.training_school.models.course import Course
from homework_03.training_school.models.student import Student


def training_school() -> None:
    courses = []

    def add_course():

        courses.append(
            Course(
                title=input("\tInput the Name of the Course:\n"),
                form=input("\tInput the Form of the Course:\n")
            )
        )

    def list_courses():

        try:
            assert len(courses) > 0
        except AssertionError:
            print("\tEmpty list of Courses. Please register a Course first.\n")

        for c, course in enumerate(courses):
            print(
                f"""
                List of registered Courses:
                ID: {c+1}
                TITLE: {course.title.capitalize()}
                FORM: {course.form.capitalize()}
                """
            )

    def remove_course():

        while True:
            try:
                assert len(courses) > 0
                course_name = input("\tInput the Name of the Course to be removed:\n")

                try:
                    assert len(course_name) > 0
                    for c, course in enumerate(courses):
                        if course.title.capitalize() == course_name.capitalize():
                            courses.pop(c)

                        print(
                            f"""
                            Course {course.title.capitalize()} removed:
                            ID: {c + 1}
                            TITLE: {course.title.capitalize()}
                            FORM: {course.form.capitalize()}
                            """
                        )

                except AssertionError:
                    print("\tMissing Course title. Please pass a Course title.\n")
                    break

            except AssertionError:
                print("\tEmpty list of Courses. Please register a Course first.\n")
                break

    def add_student():
        pass

    def list_students():
        pass

    def remove_student():
        pass

    menu_prompt = """
        Cwiczenie R2:
        
        1 - Add a Course
        2 - List Courses
        3 - Remove a Course
        4 - Add a Student to the Course
        5 - Show Courses along with list of Students
        6 - Remove Student from Course
        7 - Exit
        
        Enter your choice:\n
        """

    menu_options = {
        "1": add_course,
        "2": list_courses,
        "3": remove_course,
        "4": add_student,
        "5": list_students,
        "6": remove_student
    }

    def menu() -> None:
        """
        :return: None
        """

        while (selection := input(menu_prompt)) != "7":
            try:
                if selection == "1":
                    menu_options[selection]()
                if selection == "2":
                    menu_options[selection]()
                if selection == "3":
                    menu_options[selection]()
                if selection == "4":
                    menu_options[selection]()
                if selection == "5":
                    menu_options[selection]()
                if selection == "6":
                    menu_options[selection]()
            except KeyError:
                print("Invalid input selected. Please try again.")

    menu()
