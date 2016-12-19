# Crypto
Caesar and Vigenère cipher POC implemented in Python 3.5.2

# Background:
+ caeser cipher algorithm is simple to implement, but susceptible to frequency analysis, or brute-force attack at the very least
	+ vigen[e accente-gue]re is an example of a more complex substitution cipher
	+ uses multiple shift values rather than one, utilizing a string key rather than a single value
	+ despite this, it is still susceptible to being broken, if the attacker is aware of the length of the cipher key
		+ the cipher text is simply treated as the product of an interwoven caeser ciphers
			+ repeated cipher text patterns indicate repeated terms in the unencrypted text message
	+ whereas caeser cipher presents 25 possibilities to evaluated, vigenere presents [(26^n) - 1], possibilites
		+ where 'n' is length of the unknown key, and (-1) removes the possibility of a key composed entirely from a single character 
		+ difficult, but feasible for a dedicated attacker

# To Do:
+ clean up vigenere.py cipher function signature
	+ multiple embedded if/else should be done away with and simplified
	+ add comments

+ modify alphabet_position() and rotate_character() functions
	+ apply dictionary type
		+ decide between:
			+ dictionary methods (20.2)
			+ aliasing and copying (20.3)
			+ and sparse matrices (20.4)
		+ refer to: http://openbookproject.net/thinkcs/python/english3e/dictionaries.html 

+ add testEqual modules to crypto directory
	+ document installation and environment setup README.md

+ improve test stubs
	+ modify to operate through 'for' loops
		+ $i will iterate through alphabet chars
	+ use rand() to generate random 'rots'
		+ $x should correspond to rand() so as to produce 'expected' test result

+ modify string-to-character functions
	+ simplify by using type conversion via type constructor list()

