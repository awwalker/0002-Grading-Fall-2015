import unittest
import secret_messages as sm

class Tester(unittest.TestCase):
	def test_encrypt(self):
		self.assertEqual(sm.encrypt("Z", 3), "C")
		self.assertEqual(sm.encrypt("A", 3), "D")
		self.assertEqual(sm.encrypt("ABC", 3), "DEF")

		self.assertEqual(sm.encrypt("Hello There", 3), "Khoor Wkhuh")
		self.assertEqual(sm.encrypt("Oxen and Zebra", 3), "Rahq dqg Cheud")

		self.assertEqual(sm.encrypt("a! b! c!", 10), "k! l! m!")

#####################################

	def test_decrypt(self): #just reverse inputs and outputs from above
		self.assertEqual(sm.decrypt("C", 3), "Z")
		self.assertEqual(sm.decrypt("D", 3), "A")
		self.assertEqual(sm.decrypt("DEF", 3), "ABC")

		self.assertEqual(sm.decrypt("Khoor Wkhuh", 3), "Hello There")
		self.assertEqual(sm.decrypt("Rahq dqg Cheud", 3), "Oxen and Zebra")

		self.assertEqual(sm.decrypt("k! l! m!", 10), "a! b! c!")

		self.assertEqual(sm.decrypt("Vhfuhw", 3), "Secret")

if __name__ == '__main__':
	unittest.main()
