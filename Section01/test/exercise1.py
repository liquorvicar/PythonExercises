import unittest
from Section01.main import issue_greeting


class TestStringMethods(unittest.TestCase):

    def testHello(self):
        output = issue_greeting('Andy')
        self.assertIn('Andy', output)


if __name__ == '__main__':
    unittest.main()
