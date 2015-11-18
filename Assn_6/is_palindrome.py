"""
is_palindrome.py (4 points)
=====

Determine whether or not a string is a palindrome.

http://en.wikipedia.org/wiki/Palindrome 

For our purposes, strings that are palindromes are strings that are the same 
backwards and forwards.  Some examples of palindromes include:

"racecar"
"straw warts"
"ABBA"

For this assignment, write two functions:

1. reverse(s)
   a. reverses the order of the characters in a string...
   b. takes a string as an argument
   c. returns a new string with the letters of the original reversed
   d. "hello" would return "olleh"
   e. "" returns ""
   f. write at least two assertions for this
2. is_palindrome(s)
   a. determines whether or not the supplied string is a palindrome
   b. takes a string as an argument
   c. returns a boolean value: True if the string is a palindrome, False 
      otherwise
   d. use the above reverse function to help determine whether it is a
      palindrome or not
   e. write at least two asssertions (one for a True case and one for a False
      case)
"""
"""
Hyunkuk Lim
Intro to Computer Programming Section 10
11/1/15
"""
# define string reversing function
def reverse(s):
    line = s[-1:-(len(s)+1):-1]
    return line

# test if it works
assert reverse('racecar') == 'racecar', 'does not work properly'
assert reverse('CSCI-UA') == 'AU-ICSC', 'spaces should be removed'

# define to see if the reverse is equal to original
def is_palindrome(s):
    if s == reverse(s):
        return True
    else:
        return False

# test if it works
assert is_palindrome('racecar') == True, 'does not work properly'
assert is_palindrome('hello') == False, 'should be False'
