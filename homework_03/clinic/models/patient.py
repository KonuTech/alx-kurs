class Patient:
    """
    A Class defining attributes of a Patient entity
    """
    def __init__(self, name: str, surname: str) -> None:
        """
        :param name:
        :param surname:
        :param diseases: (optional) list of Diseases, default value is an empty list
        """
        self.name = name
        self.surname = surname
        self.diseases = []
