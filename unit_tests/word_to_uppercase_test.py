import unittest
from word_to_uppercase import to_uppercase

class WordToUpperCaseTest(unittest.TestCase):
    #Test function name MUST start with 'test'
    def test_to_uppercase(self):
        word = 'Dosh'
        result = to_uppercase(word)
        self.assertEqual(result, 'DOSH')

if __name__ == '__main__':
    unittest.main()