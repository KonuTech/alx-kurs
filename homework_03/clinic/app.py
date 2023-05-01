from typing import List

from homework_03.clinic.models.clinic import Clinic
from homework_03.clinic.models.patient import Patient
from homework_03.clinic.models.disease import Disease


tab = "\t"
new_line = "\n"


def clinic() -> None:
    clinics = []

    def add_clinic(clinics: List[Clinic]) -> None:
        """
        Prompts the user to create a new Clinic object and adds it to the given list.
        :param clinics:
        :return: None
        """

        name = input(f"{tab}Input the Name of the Clinic:{new_line}")
        if not name:
            print(f"{tab}Error: Clinic Name cannot be empty.{new_line}")
            return

        city = input(f"{tab}Input the City of the Clinic:{new_line}")
        if not city:
            print(f"{tab}Error: Clinic City cannot be empty.{new_line}")
            return

        hospital = Clinic(name=name.capitalize(), city=city.capitalize())

        for c, clinic in enumerate(clinics):
            if clinic.name == hospital.name:
                print(f"{tab}Error: Clinic Name already in a list of Clinics.{new_line}")
                return

        clinics.append(hospital)
        print(
            f"""
            {tab}Clinic {hospital.name}-{hospital.city} added to the Clinics list.{new_line}
            """
        )

    def remove_clinic(clinics: List[Clinic]) -> None:
        """
        Prompts the user to provide a Name of a Clinics to be removed.
        :param clinics:
        :return: None
        """
        if len(clinics) == 0:
            print(f"{tab}Empty list of Clinics. Please register a Clinic first.{new_line}")
            return

        clinic_name = input("\tInput the Name of the Clinic to be removed:\n")
        if not clinic_name:
            print("\tMissing Clinic's Name. Please pass a Clinic's Name.\n")
            return

        for c, clinic in enumerate(clinics):
            if clinic.name == clinic_name.capitalize():
                clinics.pop(c)
                print(f"{tab}Clinic {clinic.name} removed from the list of registered Clinics.{new_line}")
                print(
                    f"""
                    Clinic {clinic.name} removed:
                        ID: {c + 1}
                        NAME: {clinic.name}
                        CITY: {clinic.city}
                        STUDENTS: {clinic.patients}
                    """
                )

    def add_patient(clinics: List[Clinic]) -> None:
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

    def remove_patient(clinics: List[Clinic]):
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

    def list_clinics(clinics: List[Clinic]):
        """
                Prompts the user to list all registered Clinics.
                :param clinics:
                :return: None
                """
        if len(clinics) == 0:
            print(f"{tab}Empty list of Clinics. Please register a Clinic first.{new_line}")
            return

        for c, clinic in enumerate(clinics):
            print(
                f"""
                        List of registered Courses:
                        ID: {c + 1}
                        NAME: {clinic.name}
                        CITY: {clinic.city}
                        PATIENTS: {clinic.patients}
                        """
            )

    def list_patients(clinics: List[Clinic]):
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

    menu_prompt = """
        Cwiczenie R2:

        1 - Add a Clinic
        2 - Remove Clinic
        3 - Add a Patient
        4 - Remove a Patient
        5 - List Clinics
        6 - List Clinics along with registered Patients
        7 - Exit

        Enter your choice:\n
        """

    menu_options = {
        "1": add_clinic,
        "2": remove_clinic,
        "3": add_patient,
        "4": remove_patient,
        "5": list_clinics,
        "6": list_patients
    }

    def menu() -> None:
        """
        :return: None
        """

        while (selection := input(menu_prompt)) != "7":
            if selection == "1":
                menu_options[selection](clinics)
            elif selection == "2":
                menu_options[selection](clinics)
            elif selection == "3":
                menu_options[selection](clinics)
            elif selection == "4":
                menu_options[selection](clinics)
            elif selection == "5":
                menu_options[selection](clinics)
            elif selection == "6":
                menu_options[selection](clinics)
            else:
                print("Invalid input selected. Please try again.")

    menu()
