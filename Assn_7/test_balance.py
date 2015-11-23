import unittest
from balance import balanced_parentheses as bp
class Tester(unittest.TestCase):
	#Test cases provided in file
	def test_parentheses(self):
		#All should return true...
		self.assertTrue(bp('(()()()())'))
		self.assertTrue(bp('(((())))'))
		self.assertTrue(bp('(()((())()))'))
		self.assertTrue(bp('(((()))()(()()))'))
		###################################
		#All should return false...

		self.assertFalse(bp(')('))
		self.assertFalse(bp('((((((((()'))
		self.assertFalse(bp('())'))
		self.assertFalse(bp('(()())())'))
		self.assertFalse(bp('())('))
		self.assertFalse(bp(')(()'))

if __name__ == '__main__':
	unittest.main()