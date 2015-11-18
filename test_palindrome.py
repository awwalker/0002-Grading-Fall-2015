import is_palindrome as pali
import unittest

class Tester(unittest.TestCase):

    def test_reversal(self):

        self.assertEqual(pali.reverse("Table"), "elbaT")
        self.assertEqual(pali.reverse("Aaron"), "noraA")

        self.assertEqual(pali.reverse("racecar"), "racecar")
		
    def test_is_palindrome(self):
        self.assertTrue(pali.is_palindrome("racecar"))
        self.assertTrue(pali.is_palindrome("ABBA"))
        self.assertFalse(pali.is_palindrome("crap"))

if __name__ == "__main__":
    unittest.main()
