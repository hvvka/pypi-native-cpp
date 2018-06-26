import unittest

from example.functions import factorial, is_palindrome


class TestFunctions(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(3628800, factorial(10))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertFalse(is_palindrome('eleven'))


if __name__ == '__main__':
    unittest.main()
