# alphabet_position()
##
## A helper function
##
## Receives a letter (i.e. a string with only one alphabetic
## character) and returns the 0-indexed position of
## that letter within the alphabet.
##
## Should be case-insensitive (i.e. both 'a' and 'A' are index 0).
#
#
# Rather than manually creating/typing out two distinct upper/lower
# alphabet strings to check stdin against, the string.py
# module provides the following constants:
#
## string.ascii_lowercase
## string.ascii_uppercase
## string.ascii_letters, which is a concatenation of the
## previous two
#
import string

def alphabet_position(letter):
    if string.ascii_letters.index(letter) <= 25:
        return string.ascii_letters.index(letter)
    else:
        return (string.ascii_letters.index(letter) - 26)


##test stub
###uncomment to validate code
#from testEqual import testEqual
### lowercase test #1
#testEqual.testEqual(alphabet_position('a'), 0)
### uppercase test #1
#testEqual.testEqual(alphabet_position('A'), 0)
### lowercase test #2
#testEqual.testEqual(alphabet_position('b'), 1)
### lowercase test #3
#testEqual.testEqual(alphabet_position('y'), 24)
### lowercase test #4
#testEqual.testEqual(alphabet_position('z'), 25)
### uppercase test #2
#testEqual.testEqual(alphabet_position('Z'), 25)


# rotate_character()
##
## A helper function
##
## Receives a character (char) argument that is a string of
## length 1, and rotation argument (rot) that is an integer.
## Returns a new string of length 1, the result of rotating
## char by rot number of places to the right; case is preserved.
##
## Non-ASCII chars are returned unmodified, with the rotation
## argument (rot) ignored.
#
#
# The rotation algorithm (i.e. returned string) takes two forms:
#
## 1. If character shift by rotation argument (rot) is within
## ascii string index limit:
##      new_character = old_character + rotation_arg
## 2. If character shift by rotation argument (rot) exceeds the
## ascii string index limit:
##      new_character = (old_character + rotation_arg)%26
## 
# where the value 26 represents the length of the string.py
# constants -- string.ascii_lowercase and string.ascii_uppercase
#
def rotate_character(char, rot):
    if str.islower(char):
        if alphabet_position(char) + rot <= 25:
            return string.ascii_lowercase[alphabet_position(char) + rot]
        else:
            return string.ascii_lowercase[(alphabet_position(char) + rot)%26]
    elif str.isupper(char):
        if alphabet_position(char) + rot <= 25:
            return string.ascii_uppercase[alphabet_position(char) + rot]
        else:
            return string.ascii_uppercase[(alphabet_position(char) + rot)%26]
    else:
        return char


##test stub
###uncomment to validate code
#from testEqual import testEqual
### char 'a' test #1
#testEqual.testEqual(rotate_character('a', 13), 'n')
### char 'a' test #2
#testEqual.testEqual(rotate_character('a', 14), 'o')
### char 'a' test #3
#testEqual.testEqual(rotate_character('a', 0), 'a')
### char 'c' test #1
#testEqual.testEqual(rotate_character('c', 26), 'c')
### char 'c' test #2
#testEqual.testEqual(rotate_character('c', 27), 'd')
### char 'A' test #1
#testEqual.testEqual(rotate_character('A', 13), 'N')
### char 'z' test #1
#testEqual.testEqual(rotate_character('z', 1), 'a')
### char 'z' test #2
#testEqual.testEqual(rotate_character('z', 37), 'k')
### char 'Z' test #1
#testEqual.testEqual(rotate_character('Z', 2), 'B')
### char '!' test #1
#testEqual.testEqual(rotate_character('!', 37), '!')
### char '6' test #1
#testEqual.testEqual(rotate_character('6', 13), '6')
