class Clinic:
    """
    A Class defining attributes of a Clinic entity
    """
    def __init__(self, name: str, city: str) -> None:
        """
        :param name:
        :param city:
        :param patients: (optional) list of Patients, default value is an empty list
        """
        self.name = name
        self.city = city
        self.patients = []
