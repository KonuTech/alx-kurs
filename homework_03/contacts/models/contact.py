from typing import List

class Contact:

    def __init__(self, name: str, surname: str, phones: List, emails: List) -> None:
        self.name = name
        self.surname = surname
        self.phones = phones
        self.emails = emails
