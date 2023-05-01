from typing import List

from homework_03.clinic.models.clinic import Clinic
from homework_03.clinic.models.disease import Disease
from homework_03.clinic.models.patient import Patient

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
        if len(clinics) == 0:
            print("\tEmpty list of Clinics. Please register a Clinic first.\n")
            return

        clinic_name = input("\tInput the Name of the Clinic to which Patient is going to be assigned:\n")
        if not clinic_name:
            print("\tMissing Clinic's Name. Please pass a Clinic Name.\n")
            return

        name = input(f"{tab}Input a Name of a Patient:{new_line}")
        if not name:
            print(f"{tab}Error: Patient's Name cannot be empty.{new_line}")
            return

        surname = input(f"{tab}Input a Surname of a Patient:{new_line}")
        if not surname:
            print(f"{tab}Error: Patient's Surname cannot be empty.{new_line}")
            return

        # diseases = input(f"{tab}Input a Disease name of a Patient:{new_line}")
        # if not diseases:
        #     print(f"{tab}Error: Patient's Disease name cannot be empty.{new_line}")
        #     return

        sick = Patient(
            name=name.capitalize(),
            surname=surname.capitalize(),
        )

        for c, clinic in enumerate(clinics):
            if clinic.name == clinic_name.capitalize():
                clinic.patients.append(sick)

                print(
                    f"""
                         {tab}Patient:
                         {sick.name}
                         {sick.surname}
                         added to the list of Patients.{new_line}
                     """
                )

    def remove_patient(clinics: List[Clinic]):
        if len(clinics) == 0:
            print("\tEmpty list of Clinics. Please register a Clinic first.\n")
            return

        clinic_name = input("\tInput the Name of the Clinic from which Patient is going to be deleted:\n")
        if not clinic_name:
            print("\tMissing Clinic's Name. Please pass Clinic's Name.\n")
            return

        surname = input(f"{tab}Input a Surname of a Patient to be deleted:{new_line}")
        if not surname:
            print(f"{tab}Error: Patient's Surname cannot be empty.{new_line}")
            return

        for c, clinic in enumerate(clinics):
            if clinic.name == clinic_name.capitalize():
                for p, patient in enumerate(clinic.patients):
                    if patient.surname == surname.capitalize():
                        clinic.patients.remove(patient)

                        print(
                            f"""
                                {tab}Patient:
                                {patient.name}
                                {patient.surname}
                                deleted from the list of Patients.{new_line}
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
        for c, clinic in enumerate(clinics):
            print(
                f"""
                 Clinic {clinic.name}:
                     ID: {c + 1}
                     NAME: {clinic.name}
                     CITY: {clinic.city}
                 """
            )
            for p, patient in enumerate(clinic.patients):
                print(
                    f"""
                         {tab}Student:
                         {patient.name}
                         {patient.surname}
                         {patient.diseases}
                         {new_line}
                     """
                )

    def add_disease(clinics: List[Clinic]):
        if len(clinics) == 0:
            print("\tEmpty list of Clinic. Please register a Clini first.\n")
            return

        clinic_name = input("\tInput the Name of the Clinic from which Patient is going to be deleted:\n")
        if not clinic_name:
            print("\tMissing Clinic's Name. Please pass Clinic's Name.\n")
            return

        surname = input("\tInput Surname of the Patient to which Disease is going to be assigned:\n")
        if not surname:
            print("\tMissing Patient's Surname. Please pass Patient Surname.\n")
            return

        disease = input(f"{tab}Input a Name of a Disease:{new_line}")
        if not disease:
            print(f"{tab}Error: Patient's Disease Name cannot be empty.{new_line}")
            return

        sickness = Disease(
            name=disease.capitalize(),
        )

        for c, clinic in enumerate(clinics):
            if clinic.name == clinic_name.capitalize():
                for p, patient in enumerate(clinic.patients):
                    if patient.surname == surname.capitalize():
                        patient.diseases.append(sickness)

                        print(
                            f"""
                           {tab}Disease added to the Patient:
                           {patient.name}
                           {patient.surname}
                           {patient.diseases}{new_line}
                            """
                        )

    def list_diseases(clinics: List[Clinic]):
        for c, clinic in enumerate(clinics):
            print(
                f"""
                 Clinic {clinic.name}:
                     ID: {c + 1}
                     NAME: {clinic.name}
                     CITY: {clinic.city}
                 """
            )
            for p, patient in enumerate(clinic.patients):
                print(
                    f"""
                    {tab}Patient:
                    {patient.name}
                    {patient.surname}
                    {new_line}
                    """
                )
                for d, disease in enumerate(patient.diseases):
                    print(
                        f"""
                        {tab}Disease:
                        {disease.name}
                        {new_line}
                        """
                    )

    menu_prompt = """
        Cwiczenie R2:

        1 - Clinic
        2 - Patient
        3 - Exit

        Enter your choice:\n
        """

    clinic_menu_prompt = """
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

    patient_menu_prompt = """
        Cwiczenie R2:

        1 - Add a Disease
        2 - List Patient's Diseases
        3 - Exit

        Enter your choice:\n
        """

    clinic_menu_options = {
        "1": add_clinic,
        "2": remove_clinic,
        "3": add_patient,
        "4": remove_patient,
        "5": list_clinics,
        "6": list_patients
    }

    patient_menu_options = {
        "1": add_disease,
        "2": list_diseases,
    }

    def menu() -> None:
        """
        :return: None
        """

        while (selection := input(menu_prompt)) != "3":
            if selection == "1":
                while (selection := input(clinic_menu_prompt)) != "7":
                    if selection == "1":
                        clinic_menu_options[selection](clinics)
                    elif selection == "2":
                        clinic_menu_options[selection](clinics)
                    elif selection == "3":
                        clinic_menu_options[selection](clinics)
                    elif selection == "4":
                        clinic_menu_options[selection](clinics)
                    elif selection == "5":
                        clinic_menu_options[selection](clinics)
                    elif selection == "6":
                        clinic_menu_options[selection](clinics)
                    else:
                        print("Invalid input selected. Please try again.")
            elif selection == "2":
                while (selection := input(patient_menu_prompt)) != "3":
                    if selection == "1":
                        patient_menu_options[selection](clinics)
                    elif selection == "2":
                        patient_menu_options[selection](clinics)
                    else:
                        print("Invalid input selected. Please try again.")
            else:
                print("Invalid input selected. Please try again.")

    menu()
