import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_zero(self):
        self.assertEqual(add(0, 7), 7)

if __name__ == '__main__':
    unittest.main()