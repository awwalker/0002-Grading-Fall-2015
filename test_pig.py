import unittest
from pig_latin import to_pig_latin as pl

class Tester(unittest.TestCase):
	def test_pig_trivial(self):
		#self.assertEqual(pl("u mad bro"), "u mad bro") #no change to strings with spaces
		#self.assertEqual(pl("42"), "42") #no change to numbers
		#self.assertEqual(pl("aaarrooonnn!"), "aaarrooonnn!") #no change with punctuation
		#self.assertEqual(pl(""), "") #empty string returns empty string
		self.assertEqual(pl("a"), "a") #one character string

################################
	def test_pig_semi(self):
		self.assertEqual(pl("chillax"), "illaxchay") #ch removed and added to end with ay at end 
		self.assertEqual(pl("cheeks"), "eekschay")
		self.assertEqual(pl("thimble"), "imblethay") #th removed and added....
		self.assertEqual(pl("qalifornia"), "liforniaqaay") #qa removed and added...
		self.assertEqual(pl("street"), "treetsay" )
		self.assertEqual(pl("streets"), "treetssay")
		self.assertEqual(pl("Aaron"), "aaronway")
################################
	def test_pig_formal(self):
		self.assertEqual(pl("aaron"), "aaronway") #words starting with vowels append way
		self.assertEqual(pl("yolo"), "oloyay") #consonant taken away from front appened at end
		self.assertEqual(pl("narwhal"), "arwhalnay") # " "


if __name__ == '__main__':
	unittest.main()