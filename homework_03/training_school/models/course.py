class Course:
    """
    A Class defining attributes of a Course entity
    """
    def __init__(self, title: str, city: str, date: str) -> None:
        """
        :param title:
        :param city:
        :param date:
        :param students: (optional) list of students enrolled in the course, default value is an empty list
        :param teachers: (optional) list of teachers for the course, default value is an empty list
        """
        self.title = title
        self.city = city
        self.date = date
        self.students = []
        self.teachers = []
