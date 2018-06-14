import unittest
from Section01.main import get_length


class TestStringLength(unittest.TestCase):

    def testEmptyString(self):
        self.assertEqual(get_length(''), 0)

    def testSingleChar(self):
        self.assertEqual(get_length('a'), 1)

    def testLongerString(self):
        self.assertEqual(get_length('seven'), 5)

    def testLongestString(self):
        self.assertEqual(get_length('abcdefghijklmnopqrstuvwxyz'), 26)


if __name__ == '__main__':
    unittest.main()

