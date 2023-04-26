class Course:
    """
    A Class defining attributes of a Course
    """
    def __init__(self, title: str, form: str) -> None:
        """
        :param title:
        :param form:
        """
        self.title = title
        self.form = form
        self.students = []
