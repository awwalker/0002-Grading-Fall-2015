"""
string_practice.py (4 points)
=====
Follow the directions underneath each comment below:
"""
"""
Hyunkuk Lim
Intro to Computer Programming Section 10
11/1/15
"""
# Part 1 (1 point)
# =======
# Create two strings, "123" and "\n  marshmallows\n  ", assign them to the
# variables, numbers and food, respectively (keep ths spaces and new lines).
#
# Use the method that gives back the uppercase version of a string on your
# variable food. Save the result into a variable named result. Print out both
# variables, result and food.

# define the variables
numbers = '123'
food = "\n  marshmallows\n  "

# save the uppercase version into a variable
result = food.upper()
# print original and result of changing to upper
print(food)
print(result)

# Part 2 (1 point)
# =======
# Print out the results of calling the methods that do the following:
# * tests if your numbers variable consists of only digits
# * tests if your numbers variable consists of only letters
# * tests if your numbers variable is uppercase (should be false!)
# * tests if your food variable is lowercase

# see if it is all numbers
print(numbers.isdigit())
# see if it is all letters
print(numbers.isalpha())
# see if it is uppercase
print(numbers.isupper())
# see if it is lowercase
print(food.islower())

# Part 3 (1 point)
# =======
# Use the method that gives back the index of a substring from within a
# a larger string to print out the following:
# * call the method to get the index of "mall" in the variable, food... and
#   print out the result
# * call the method again to get the index of "camping" in the variable, food
#   (this should still give back a value, -1!)... and print out the result
#
# Finally use the operator that gives back a boolean if a substring occurs
# within another. Do this to find out of the string "4" is in your string
# variable, numbers.

# give index for mall
print(food.find('mall'))
# give index for camping, which does not exist and gives -1
print(food.find('camping'))
# see if 4 is in variable numbers
print('4' in numbers)

# Part 4 (1 point)
# =======
# * print out the result of calling the method that removes white space
#   from the beginning and end of your variable, food
# * print out the result of calling the format method on the string,
#   "{0} agitated ants and {1} anxious antelopes" ... and using the numbers
#   24 and 48 as the variables that get placed inot the placeholders

# remove all spaces
print(food.strip())
# define 24 and 48 into variables
num_1 = '24'
num_2 = '48'
# define the sentence into a variable
sentence = "{0} agitated ants and {1} anxious antelopes"

# replace 48 into {1}
new = sentence.format(num_1, num_2)
# print the new sentence with replacements
print(new)
