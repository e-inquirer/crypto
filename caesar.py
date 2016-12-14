# alphabet_position()
##
## A helper function
##
## Receives a letter (i.e. a string with only one alphabetic
## character) and returns the 0-based numerical position of
## that letter within the alphabet.
##
## Should be case-insensitive (i.e. both 'a' and 'A' are index 0).
#
#
# Rather than manually creating/typing out two distint upper/lower
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


#test stub
##uncomment to validate code
from testEqual import testEqual
## lowercase test #1
testEqual.testEqual(alphabet_position('a'), 0)
## uppercase test #1
testEqual.testEqual(alphabet_position('A'), 0)
## lowercase test #2
testEqual.testEqual(alphabet_position('b'), 1)
## lowercase test #3
testEqual.testEqual(alphabet_position('y'), 24)
## lowercase test #4
testEqual.testEqual(alphabet_position('z'), 25)
## uppercase test #2
testEqual.testEqual(alphabet_position('Z'), 25)

