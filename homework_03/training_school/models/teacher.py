class Teacher:
    """
    A Class defining attributes of a Teacher entity
    """
    def __init__(self, name: str, surname: str, specialization: str) -> None:
        """
        :param name:
        :param surname:
        :param specialization:
        """
        self.name = name
        self.surname = surname
        self.specialization = specialization
