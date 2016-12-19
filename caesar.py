# import helper functions from ./helpers.py
#
from helpers import alphabet_position, rotate_character

# encrypt()
#
## Caeser cipher function signature
## 
## Receives two arguments, a string (text) and an integer (rot).
##
## Returns the result of rotating each letter in the text by rot
## places to the right.
##
## Non-alphabetic characters (e.g. space, numbers, symbols) are
## left as is.
##
## Calls rotate_character() function.
#
def encrypt(text, rot):
    novusText = ''
    
    for i in range(len(text)):
        novusText += rotate_character(text[i], rot)

    return novusText


##test stub
###uncomment to validate code
#from testEqual import testEqual
### test #1
#testEqual.testEqual(encrypt('a', 13), 'n')
### test #2
#testEqual.testEqual(encrypt('abcd', 13), 'nopq')
### test #3
#testEqual.testEqual(encrypt('LaunchCode', 13), 'YnhapuPbqr')
### test #4
#testEqual.testEqual(encrypt('LaunchCode', 1), 'MbvodiDpef')
### test #5
#testEqual.testEqual(encrypt('Hello, World!', 5), 'Mjqqt, Btwqi!')


## User input
#usrTXT = input("Type a message: ")
#usrROT = int(input("Rotate by: "))
#
## Encrypt user input using caesar cipher, then print to STDOUT
#print(encrypt(usrTXT, usrROT))

# User input
## ROT as cmd-line arg
## Validation
#
import sys

def user_input_is_valid(cl_args):
    if (len(cl_args)  > 1) and str.isdigit(cl_args[1]):
        return True
    else:
        return False 
    
if user_input_is_valid(sys.argv):
    usrROT = int(sys.argv[1])
    usrTXT = input("Type a message: ")

# Encrypt user input using caesar cipher, then print to STDOUT
    print(encrypt(usrTXT, usrROT))
else:
    print("usage: python3 caesar.py n")


