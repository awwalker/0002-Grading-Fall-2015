"""
pig_latin.py (6 points)
=====

Write a function called to_pig_latin that translates a word into pig latin. 

http://en.wikipedia.org/wiki/Pig_Latin

IPO for to_pig_latin function
-----
input (parameters): a string
processing: convert the string into pig latin
output (return value): a new string (in pig latin)

Our version of Pig Latin will follow these rules:
-----
* _IGNORE ANY STRING WITH NON-LETTER CHARACTERS_ (including spaces); it should
  just return the original string
* _THIS FUNCTION WILL NOT BREAK A STRING INTO SEPARATE WORDS_
* all letters automatically get converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels? you can check if a character exists within a 
  string of all vowels
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

Example:
-----
print(to_pig_latin(s))
# prints out...
"""
"""
Hyunkuk Lim
Intro to Computer Programming Section 10
11/1/15
"""
# define the function
def to_pig_latin(s):
    # make the argument all lowercase
    s = s.lower()
    # return original if the argument's length is less than or equal to one
    if len(s) <= 1:
        return s
    # return original if the argument has something other than alphabets
    elif s.isalpha == False:
        return s
    # if it starts with a vowel, add way to the end of the argument
    elif s[0] in 'aeiou':
        s += 'way'
        return s
    # if it starts with sh, ch, th, or qa, move the first two characters to
    # the end and add ay to the changed argument
    elif s[:2] in 'sh ch th qa':
        s = s[2:len(s)] + s[0:2] + 'ay'
        return s
    # if the argument does not belong to any of the categories above, move
    # the first letter to the end and add ay to the changed argument
    else:
        s = s[1:len(s)] + s[0] + 'ay'
        return s

# test some cases to see if it works
assert to_pig_latin('') == '', 'returns empty strings'
assert to_pig_latin('s') == 's', 'returns single character'
assert to_pig_latin('at') == 'atway', 'words that start with a vowel have way added'
assert to_pig_latin('thimble') == 'imblethay', 'words that start with sh, ch, th, or qa have the start moved to back and have ay added'
assert to_pig_latin('correct') == 'orrectcay', 'other words have the start moved to back and have ay added'

