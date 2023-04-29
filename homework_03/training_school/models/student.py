class Student:
    """
    A Class defining attributes of a Student entity
    """
    def __init__(self, name: str, surname: str, phone: str, email: str) -> None:
        """
        :param name:
        :param surname:
        """
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
