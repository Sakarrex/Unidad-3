from msilib.schema import Class
from typing_extensions import Self
import unittest
from ClasePalindromo import Palindromo


class TestPalindromos(unittest.TestCase):
    __unPalindromo = Palindromo("vacio")
    def test_ana(self):
        self.__unPalindromo.setPalabra("ana")
        self.assertTrue(self.__unPalindromo.esPalindromo)
    def test_ANA(self):
        self.__unPalindromo.setPalabra("ANA")
        self.assertTrue(self.__unPalindromo.esPalindromo)
    def test_anana(self):
        self.__unPalindromo.setPalabra("anana")
        self.assertTrue(self.__unPalindromo.esPalindromo)
    def test_MENEM(self):
        self.__unPalindromo.setPalabra("MENEM")
        self.assertTrue(self.__unPalindromo.esPalindromo)
    def test_MENEM(self):
        self.__unPalindromo.setPalabra("MENEm")
        self.assertTrue(self.__unPalindromo.esPalindromo)
    def test_marcos(self):
        self.__unPalindromo.setPalabra("marcos")
        self.assertFalse(self.__unPalindromo.esPalindromo)
    def test_Marcos(self):
        self.__unPalindromo.setPalabra("Marcos")
        self.assertFalse(self.__unPalindromo.esPalindromo)