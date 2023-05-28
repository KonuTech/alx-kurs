import unittest
import calc


class CalcTest(unittest.TestCase):

    def testSuma(self):
        wynik = calc.suma(3, 5)
        self.assertEqual(wynik, 8)

        wynik = calc.suma(5, 5)
        self.assertEqual(wynik, 10)

    def testRoznica(self):
        wynik = calc.roznica(4, 2)
        self.assertEqual(wynik, 2)

    def testIloczyn(self):
        wynik = calc.iloczyn(4, 3)
        self.assertEqual(wynik, 12)

    def testIloraz(self):
        wynik = calc.iloraz(4, 0)
        self.assertRaises(ZeroDivisionError, wynik)

        wynik = calc.iloraz(4, 2)
        self.assertEqual(wynik, 2)
