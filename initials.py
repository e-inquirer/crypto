# Given a person's name, return the person's initials (uppercase)
def get_initials(fullname):
    fullname = fullname.split(' ')
    initials = ''

# accumulator pattern
    for eachName in fullname:
        initials = initials + eachName[0].upper()
    
    return initials

inputName = input("What is your full name?\n")
print(get_initials(inputName))

# test stub
## uncomment to validate code

#from testEqual import testEqual
### test: "First Last"
#testEqual.testEqual(get_initials("Ozzie Smith"), "OS")
### test: "first last"
#testEqual.testEqual(get_initials("bonnie blair"), "BB")
### test: "First Middle Last"
#testEqual.testEqual(get_initials("Daniel Day Lewis"), "DDL")

