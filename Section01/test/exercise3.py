import unittest
from Section01.main import get_quote_string


class TestQuoteString(unittest.TestCase):

    def testErrorsWithNoQuote(self):
        self.assertRaises(AssertionError, get_quote_string, '', 'Author')

    def testErrorsWithNoAuthor(self):
        self.assertRaises(AssertionError, get_quote_string, 'I will survive', '')

    def testReturnsQuoteInQuotes(self):
        self.assertEqual(get_quote_string('I will survive', 'Gloria Gaynor'), 'Gloria Gaynor says "I will survive"')
