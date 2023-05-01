class Student:

    def __init__(self, name: str, surname: str, group: int) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        return self.grades.append(grade)

    def list_grades(self):
        for g, grade in enumerate(self.grades):
            print(grade, end=", ")

    def get_average(self):
        sum = 0
        grades_frequency = len(self.grades)
        for g, grade in enumerate(self.grades):
            sum += grade

        return sum / grades_frequency
