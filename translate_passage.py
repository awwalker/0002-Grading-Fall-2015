"""
translate_passage.py (6 points)
=====

Use your to_pig_latin function to translate an entire passage of text. Do this
by importing your pig_latin module, and calling your to_pig_latin function.

You can use Mary Shelley's Frankenstein from Project Gutenberg:
http://www.gutenberg.org/cache/epub/84/pg84.txt

The second paragraph in the first letter is:
-----
I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight. ...

Would be translated to...
-----
i amway alreadyway arfay orthnay ofway ondonlay, andway asway i alkway inway 
ethay treetssay ofway etersburghpay, i eelfay a oldcay orthernnay reezebay 
laypay uponway ymay eekschay, hichway racesbay ymay ervesnay andway illsfay 
emay ithway elightday.

1. Bring in your pig_latin module using import
2. Copy a large paragraph from Mary Shelley's Frankenstein (second 
   paragraph of first letter works well) into this file as a triple quoted
   string.  Assign this string to a variable name.
3. Write a function that will:
   a. take one input, a string, the entire passage to be translated.
   b. return a translated version of the string by using the pig latin 
      function (that only translates single words)
4. To do this treat all consecutive letters as words.  Note that numbers, 
   punctuation and whit space do not count as "letters".  Translate each word 
   and create a string that represents the translation of the full text.
5. You can use whatever algorithm you'd like to do this.
6. ...As long as the translation works accurately.
7. Print out the result of calling your translate_passage function on a 
   paragraph from Frankenstein
8. Feel free to come up with your assertions to test your function along the
   way.

HINT (though, don't read this until you've tried writing the pseudocode for
the above specifications on your own)
1. Accumulate two strings... your current word, and the actual translation.
2. Go through every character, collecting them into a word. 
3. When you encounter a non letter character (use islpha), take what you
   currently have as a word, translate it, and add it to the translation
4. Add the non letter character to the translation
5. Reset your current word to empty string and go on with the loop

(This is just one possible implementation; there are other ways to do this!)
"""
"""
Hyunkuk Lim
Intro to Computer Programming Section 10
11/1/15
"""
# import pig latin translator
import pig_latin

# define the paragraph to a variable
paragraph = """I am already far north of London, and as I walk in the streets of\
Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my\
nerves and fills me with delight."""

# define the function that translates the paragraph using pig latin
def translate(s):
    # make an accumulator to add the letters until there is a space
    word = ''
    # make an accumulator to add the translated words to print at the end
    translated = ''
    for x in s:
        # if x is a letter, add to word variable
        if x.isalpha():
            word += x
        # if x is not a letter, translate the word, add x, and reset variable
        # word for the next word
        elif x.isalpha() == False:    
            translated += pig_latin.to_pig_latin(word)
            translated += x
            word = ''
    # return the translated paragraph
    return translated
