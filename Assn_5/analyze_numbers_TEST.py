import unittest
import analyze_numbers as an

tests = [10, 4, 9, 19, 56, 945]
class Tester(unittest.TestCase):
    def test_prime(self):
        self.assertFalse(an.is_prime(10))
        self.assertFalse(an.is_prime(4))
        self.assertFalse(an.is_prime(9))
        self.assertTrue(an.is_prime(19))
        self.assertFalse(an.is_prime(56))
        self.assertFalse(an.is_prime(945))
            
    def test_odd(self):
        self.assertFalse(an.is_odd(10))
        self.assertFalse(an.is_odd(4))
        self.assertTrue(an.is_odd(9))
        self.assertTrue(an.is_odd(19))
        self.assertFalse(an.is_odd(56))
        self.assertTrue(an.is_odd(945))
        
    def test_abundant(self):
        self.assertFalse(an.is_abundant(10))
        self.assertFalse(an.is_abundant(4))
        self.assertFalse(an.is_abundant(9))
        self.assertFalse(an.is_abundant(19))
        self.assertTrue(an.is_abundant(56))
        self.assertTrue(an.is_abundant(945))
        
if __name__ == '__main__':
    unittest.main()
