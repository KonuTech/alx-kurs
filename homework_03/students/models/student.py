from typing import List


class Student:

    def __init__(self, name: str, surname: str, group: str, grades: List) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = grades

    def add_grade(self, grade, results):
        return results.append(grade)

    def list_grades(self):
        for g, grade in enumerate(self.grades):
            print(grade, end=", ")

    def get_average(self):
        sum = 0
        grades_frequency = len(self.grades)
        for g, grade in enumerate(self.grades):
            sum += grade

        return sum / grades_frequency
