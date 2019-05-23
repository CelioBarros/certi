import unittest
import sys
sys.path.insert(0,'app')
import auxiliar_function

class TestStringMethods(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(1), 'um')
        self.assertEqual(auxiliar_function.number_to_word(11), 'onze')
        self.assertEqual(auxiliar_function.number_to_word(95), 'noventa e cinco')

    def test_hundred_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(100), 'cem')
        self.assertEqual(auxiliar_function.number_to_word(110), 'cento e dez')
        self.assertEqual(auxiliar_function.number_to_word(999), 'novecentos e noventa e nove')

    def test_thousand_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(1000), 'mil')
        self.assertEqual(auxiliar_function.number_to_word(1110), 'mil e cento e dez')
        self.assertEqual(auxiliar_function.number_to_word(3112), 'três mil e cento e doze')
        self.assertEqual(auxiliar_function.number_to_word(99999), 'noventa e nove mil e novecentos e noventa e nove')

    def test_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-1), 'menos um')
        self.assertEqual(auxiliar_function.number_to_word(-8), 'menos oito')
        self.assertEqual(auxiliar_function.number_to_word(-94), 'menos noventa e quatro')

    def test_hundred_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-100), 'menos cem')
        self.assertEqual(auxiliar_function.number_to_word(-200), 'menos duzentos')
        self.assertEqual(auxiliar_function.number_to_word(-378), 'menos trezentos e setenta e oito')
        self.assertEqual(auxiliar_function.number_to_word(-930), 'menos novecentos e trinta')

    def test_thousand_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-1000), 'menos mil')
        self.assertEqual(auxiliar_function.number_to_word(-7007), 'menos sete mil e sete')
        self.assertEqual(auxiliar_function.number_to_word(-54056), 'menos cinco e quatro mil e cinquenta e seis')
        self.assertEqual(auxiliar_function.number_to_word(-99999), 'menos noventa e nove mil e novecentos e noventa e nove')

    def test_O(self):
        self.assertEqual(auxiliar_function.number_to_word(0), 'zero')

if __name__ == '__main__':
    unittest.main()