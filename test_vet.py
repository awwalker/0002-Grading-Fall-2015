import unittest
import vet
import sys

#redirect all print functions to our txt file to read after testing
f = open('animal_TEST_print.txt', 'w')
sys.stdout = f

class Tester(unittest.TestCase):
	
	#first necessary function
	#parameters: 2 - a string (name to searach for), and a list of animals
	#returns: a single animal (a list) or None if the animal is not found
	def test_find_by_name(self):
		animal_list = [['bev', 'dog', 10], ['ari', 'cat', 10], ['zim', 'dog', 10], 
		['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50],
		['jane clawston', 'cat', 10], ['franz catka', 'cat', 2], ['bark twain', 'dog', 20]]

		self.assertEqual(vet.find_by_name('gertrude', animal_list), ['gertrude', 'goat', 99]) #returns whole list
		self.assertEqual(vet.find_by_name('franz catka', animal_list), ['franz catka', 'cat', 2]) #returns whole list
		self.assertIsNone(vet.find_by_name('aaron', animal_list)) #returns None if not present

	#second necessary function
	#parameters: a list of animals
	#CANNOT USE LIST'S SORT METHOD...Has to use bubble sort
	#returns nothing
	def test_sort_by_name(self):
		animal_list_1 = [['zim', 'dog', 10], ['bev', 'dog', 10], ['ari', 'cat', 10]]
		animal_list_2 = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50], ['zim', 'dog', 10]]
		#correctly sorts standard list
		self.assertEqual(vet.sort_by_name(animal_list_1, [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]))
		self.assertEqual(vet.sort_by_name(animal_list_2, [['ang', 'unicorn', 50], ['gertrude', 'goat', 99], ['sam', 'snake', 4], ['zim', 'dog', 10] ]))

	#fourth necessary function (printing was 3rd)
	#parameters: a list of animals
	#returns: a single animal (a list)
	#should check if list of all 0 urgencies passes...
	def test_get_most_urgent(self):
		reg_animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
		zero_animal_list = [['sam', 'snake', 0]]
		self.assertEqual(vet.get_most_urgent(reg_animal_list), ['gertrude', 'goat', 99])
		self.assertEqual(vet.get_most_urgent(zero_animal_list), ['sam', 'snake', 0])

	#fifth necessary function (just reverse findings from #4)
	def test_get_least_urgent(self):
		reg_animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
		zero_animal_list = [['sam', 'snake', 0]]
		self.assertEqual(vet.get_most_urgent(reg_animal_list), ['sam', 'snake', 4])
		self.assertEqual(vet.get_most_urgent(zero_animal_list), ['sam', 'snake', 0])

	def test_allowed_animal(self):
		allowed_animals = ['dog', 'cat', 'snake', 'goat', 'pig', 'duck', 'narwhale','unicorn']
		self.assertFalse(vet.allowed_animal('alligator'))
		#TRUST NO ONE!!! (as in who knows (HA YOU WILL) if they copied everything in correctly)
		self.assertTrue(vet.allowed_animal('dog'))
		self.assertTrue(vet.allowed_animal('cat'))
		self.assertTrue(vet.allowed_animal('snake'))
		self.assertTrue(vet.allowed_animal('goat'))
		self.assertTrue(vet.allowed_animal('pig'))
		self.assertTrue(vet.allowed_animal('duck'))
		self.assertTrue(vet.allowed_animal('narwhale'))
		self.assertTrue(vet.allowed_animal('unicorn'))

	def test_print_animals(self):
		animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
		vet.print_animals(animal_list) #check output in file named above!
		#Every animal needs its position in the overal list (start at 1 not 0)
		#Every animal needs its name
		#Every animal needs its type
		self.assertIsNone(vet.print_animals(animal_list))
		"""
		prints out something close to....
		1 - sam, snake
		2 - gertrude, goat
		3 - ang, unicorn
		"""

if __name__ == '__main__':
	unittest.main()