import unittest
import contact


class ContactTest(unittest.TestCase):

    contact_1 = contact.Contat("Adam", "Nowak")
    contact_2 = contact.Contat("Tomasz", "Kowalski")

    def test_email(self):
        self.assertEqual(self.contact_1.email(), "Adam_Nowak@firma.pl")
        self.assertEqual(self.contact_2.email(), "Tomasz_Kowalski@firma.pl")

    def test_przedstawsie(self):
        self.assertEqual(self.contact_1.przedstaw_sie(), "Adam Nowak")
        self.assertEqual(self.contact_2.przedstaw_sie(), "Tomasz Kowalski")
