import unittest
import sys
sys.path.insert(0,'app')
import auxiliar_function

class TestStringMethods(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(1), 'um')

    def test_hundred_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(100), 'cem')

    def test_thousand_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(1000), 'mil')

    def test_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-1), 'menos um')

    def test_hundred_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-100), 'menos cem')

    def test_thousand_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-1000), 'menos mil')

    def test_O(self):
        self.assertEqual(auxiliar_function.number_to_word(0), 'zero')

if __name__ == '__main__':
    unittest.main()