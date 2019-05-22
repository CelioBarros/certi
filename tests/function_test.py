import unittest
import sys
sys.path.insert(0,'app')
import auxiliar_function

class TestStringMethods(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(auxiliar_function.number_to_word(1), 'um')

    def test_negative(self):
        self.assertEqual(auxiliar_function.number_to_word(-1), 'menos um')

    def test_O(self):
        self.assertEqual(auxiliar_function.number_to_word(0), 'zero')

if __name__ == '__main__':
    unittest.main()