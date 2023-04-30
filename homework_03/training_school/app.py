from typing import List

from homework_03.training_school.models.course import Course
from homework_03.training_school.models.student import Student

tab = "\t"
new_line = "\n"


def training_school() -> None:
    courses = []
    # students = []

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

        city = input(f"{tab}Input the City of the Course:{new_line}")
        if not city:
            print(f"{tab}Error: Course City cannot be empty.{new_line}")
            return

        date = input(f"{tab}Input the Date of the Course:{new_line}")
        if not date:
            print(f"{tab}Error: Course Date cannot be empty.{new_line}")
            return

        training = Course(title=title.capitalize(), city=city.capitalize(), date=date.capitalize())

        for c, course in enumerate(courses):
            if course.title == training.title:
                print(f"{tab}Error: Course Title already in a list of Courses.{new_line}")
                return

        courses.append(training)
        print(
            f"""
            {tab}Course {training.title}-{training.city}-{training.date} added to the Courses list.{new_line}
            """
        )

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
                ID: {c + 1}
                TITLE: {course.title}
                CITY: {course.city}
                DATE: {course.date}
                TEACHERS: {course.teachers}
                STUDENTS: {course.students}
                """
            )

    def remove_course(courses: List[Course]) -> None:
        """
        Prompts the user for a Title of a Course to be removed from a list of Courses.
        :param courses:
        :return: None
        """

        if len(courses) == 0:
            print("\tEmpty list of Courses. Please register a Course first.\n")
            return

        course_name = input("\tInput the Name of the Course to be removed:\n")
        if not course_name:
            print("\tMissing Course title. Please pass a Course title.\n")
            return

        for c, course in enumerate(courses):
            if course.title == course_name.capitalize():
                courses.pop(c)
                print(f"{tab}Course {course.title} removed from the list of registered Courses.{new_line}")
                print(
                    f"""
                    Course {course.title} removed:
                        ID: {c + 1}
                        TITLE: {course.title}
                        CITY: {course.city}
                        DATE: {course.date}
                        TEACHERS: {course.teachers}
                        STUDENTS: {course.students}
                    """
                )

    def add_student(courses: List[Course]):
        if len(courses) == 0:
            print("\tEmpty list of Courses. Please register a Course first.\n")
            return

        course_name = input("\tInput the Name of the Course to which Student is going to be assigned:\n")
        if not course_name:
            print("\tMissing Course title. Please pass a Course title.\n")
            return

        name = input(f"{tab}Input a Name of a Student:{new_line}")
        if not name:
            print(f"{tab}Error: Student's Name cannot be empty.{new_line}")
            return

        surname = input(f"{tab}Input a Surname of a Student:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        phone = input(f"{tab}Input a Phone number of a Student:{new_line}")
        if not phone:
            print(f"{tab}Error: Student's Phone Number cannot be empty.{new_line}")
            return

        email = input(f"{tab}Input an Email address of a Student:{new_line}")
        if not email:
            print(f"{tab}Error: Student's Email address cannot be empty.{new_line}")
            return

        pupil = Student(
            name=name.capitalize(),
            surname=surname.capitalize(),
            phone=phone,
            email=email,
        )

        for c, course in enumerate(courses):
            if course.title == course_name.capitalize():
                course.students.append(pupil)

                print(
                    f"""
                        {tab}Student:
                        {pupil.name}
                        {pupil.surname}
                        {pupil.phone}
                        {pupil.email}
                        added to the list of Students.{new_line}
                    """
                )

    def remove_student(courses: List[Course]):
        if len(courses) == 0:
            print("\tEmpty list of Courses. Please register a Course first.\n")
            return

        course_name = input("\tInput the Name of the Course from which Student is going to be deleted:\n")
        if not course_name:
            print("\tMissing Course title. Please pass a Course title.\n")
            return

        surname = input(f"{tab}Input a Surname of a Student to delete:{new_line}")
        if not surname:
            print(f"{tab}Error: Student's Surname cannot be empty.{new_line}")
            return

        for c, course in enumerate(courses):
            if course.title == course_name.capitalize():
                for s, student in enumerate(course.students):
                    if student.surname == surname.capitalize():
                        course.students.remove(student)

                        print(
                            f"""
                                {tab}Student:
                                {student.name}
                                {student.surname}
                                {student.phone}
                                {student.email}
                                deleted from the list of Students.{new_line}
                            """
                        )

    def list_students(courses: List[Course]):
        for c, course in enumerate(courses):
            print(
                f"""
                Course {course.title} removed:
                    ID: {c + 1}
                    TITLE: {course.title}
                    CITY: {course.city}
                    DATE: {course.date}
                """
            )
            for s, student in enumerate(course.students):
                print(
                    f"""
                        {tab}Student:
                        {student.name}
                        {student.surname}
                        {student.phone}
                        {student.email}
                        {new_line}
                    """
                )

    def add_teacher():
        pass

    def reassign_student():
        pass

    menu_prompt = """
        Cwiczenie R2:

        1 - Add a Course
        2 - List Courses
        3 - Remove a Course
        4 - Add a Student to the Course
        5 - Remove a Student from the Course
        6 - List Courses along with registered Students
        7 - Add a Teacher to the Course
        8 - Reassign a Student to different Course
        9 - Exit

        Enter your choice:\n
        """

    menu_options = {
        "1": create_course,
        "2": list_courses,
        "3": remove_course,
        "4": add_student,
        "5": remove_student,
        "6": list_students,
        "7": add_teacher,
        "8": reassign_student
    }

    def menu() -> None:
        """
        :return: None
        """

        while (selection := input(menu_prompt)) != "9":
            if selection == "1":
                menu_options[selection](courses)
            elif selection == "2":
                menu_options[selection](courses)
            elif selection == "3":
                menu_options[selection](courses)
            elif selection == "4":
                menu_options[selection](courses)
            elif selection == "5":
                menu_options[selection](courses)
            elif selection == "6":
                menu_options[selection](courses)
            elif selection == "7":
                menu_options[selection]()
            elif selection == "8":
                menu_options[selection]()
            else:
                print("Invalid input selected. Please try again.")

    menu()
