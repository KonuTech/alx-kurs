from typing import List

from homework_03.training_school.models.course import Course
from homework_03.training_school.models.student import Student

tab = "\t"
new_line = "\t"


def training_school() -> None:
    courses = []

    def create_course(courses: List[Course]) -> None:
        """
        Prompts the user to create a new Course object and adds it to the given list.
        :param courses:
        :return: None
        """

        title = input(f"{tab}Input the Name of the Course:{new_line}")
        if not title:
            print(f"{tab}Error: Course Title cannot be empty.{new_line}")
            return

        form = input(f"{tab}Input the Form of the Course:{new_line}")
        if not form:
            print(f"{tab}Error: Course Form cannot be empty.{new_line}")
            return

        training = Course(title=title.capitalize(), form=form.capitalize())

        for c, course in enumerate(courses):
            if course.title == training.title:
                print(f"{tab}Error: Course Title already in a list of Courses.{new_line}")
                return

        courses.append(training)
        print(f"{tab}Course {training.title}-{training.form} added to the Courses list.{new_line}")

    def list_courses(courses: List[Course]) -> None:
        """
        Prompts the user to list all registered Courses.
        :param courses:
        :return: None
        """
        if len(courses) == 0:
            print(f"{tab}Empty list of Courses. Please register a Course first.{new_line}")
            return

        for c, course in enumerate(courses):
            print(
                f"""
                List of registered Courses:
                ID: {c+1}
                TITLE: {course.title}
                FORM: {course.form}
                """
            )

    def remove_course(courses: List[Course]) -> None:

        if len(courses) == 0:
            print("\tEmpty list of Courses. Please register a Course first.\n")
            return

        course_name = input("\tInput the Name of the Course to be removed:\n")
        if not course_name:
            print("\tMissing Course title. Please pass a Course title.\n")
            return

        for c, course in enumerate(courses):
            print(c, course.title)
            if course.title != course_name.capitalize():
                print(f"{tab}Error: Course Title not in a list of registered Courses.{new_line}")
                return
            else:
                courses.pop(c)
                print(f"{tab}Course {course.title} removed from the list of registered Courses.{new_line}")
                print(
                    f"""
                    Course {course.title} removed:
                        ID: {c + 1}
                        TITLE: {course.title}
                        FORM: {course.form}
                    """
                )

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
        "1": create_course,
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
                    menu_options[selection](courses)
                if selection == "2":
                    menu_options[selection](courses)
                if selection == "3":
                    menu_options[selection](courses)
                if selection == "4":
                    menu_options[selection]()
                if selection == "5":
                    menu_options[selection]()
                if selection == "6":
                    menu_options[selection]()
            except KeyError:
                print("Invalid input selected. Please try again.")

    menu()
