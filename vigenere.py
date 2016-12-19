#### vigenere.py ####
#
# encrypt()
#
## Vigenere cipher function signature
## 
## Receives two arguments, a string (text) and a cipher key (key).
##
## Returns the result of rotating each string character in the
## text, by a value corresponding to its relative key character
## pair, rot positions to the right.
##
## Non-alphabetic characters (e.g. space, numbers, symbols) are
## left as is.
##
## Calls rotate_character() function.
#
# import helper functions from ./helpers.py
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    novusText = ''
    keyElements = []

    for i in range(len(key)):
        keyElements.append(alphabet_position(key[i]))
        
    j = 0
    import itertools
    for rotCycle in itertools.cycle(keyElements):
        if not(j < len(text)):
            break

        elif str.isalpha(text[j]):
            novusText += rotate_character(text[j], rotCycle)

            j += 1

        else:
            novusText += text[j]
            j += 1
            if j < len(text):
                novusText += rotate_character(text[j], rotCycle)
                j += 1

    return novusText


##test stub
###uncomment to validate code
#from testEqual import testEqual
### test #1
#testEqual.testEqual(encrypt("The crow flies at midnight!", "boom"), "Uvs osck rmwse bh auebwsih!")

def main():
    # User input
    usrTXT = input("Type a message: ")
    usrKEY = input("Encryption key: ")

    # Encrypt user input using vigenere cipher, then print to STDOUT
    print(encrypt(usrTXT, usrKEY))

if __name__ == '__main__':
    main()

