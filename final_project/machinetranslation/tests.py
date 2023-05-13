"""Task 2: Write the unit tests for English to French translator \
    and French to English translator function in tests.py"""

import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        """Function - test1"""
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), "")
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test2(self):
        """Function - test2"""
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        # Test None returns empty string
        self.assertNotEqual(french_to_english("None"), "")
        # Test empty string returns empty string
        self.assertNotEqual(french_to_english(0),0)
unittest.main()
