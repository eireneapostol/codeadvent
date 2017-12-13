'''
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
'''


'''
PART TWO
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
'''

f = open("./inputs/day4","r")
suma = 0
suma2 = 0
for line in f:
    line = sorted(line.split())

    line2 = []
    for word in line:
        word = sorted(word)
        line2.append(word)
    line2 = sorted(line2)

    true = 1
    true2 = 1
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            true = 0
        if line2[i] == line2[i+1]:
            true2 = 0
    suma +=1 if true else 0
    suma2 +=1 if true2 else 0

print(suma, suma2)