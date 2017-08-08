# Jeremy and Clara are learning about passwords and created a game to test their "hacking" skills. Jeremy made rules for valid passwords and Clara needs to write a program to generate all possible passwords that meet those rules. Jeremy's rules are these:
#
# - a password consists of exactly  lowercase English letters.
# - the password is melodious, meaning that consonants can only be next to vowels and vowels can only be next to consonants. Example: bawahaha
# - the password cannot contain the letter  (because it's both a consonant and vowel).
# - the first letter of the password can be either a vowel or consonant.
# image
#
# Given the length, , of the password, print all of the possible passwords that meet the conditions above.
#
# Input Format
#
# The line of input contains the integer  (the length of the password).

#!/bin/python3

import sys

# generates all possible passwords satisfying the conditions above
def allPossibleMelodius(n, isVowel):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxz"
    if isVowel:
        if n <= 1:
            return list(vowels)
        else:
            result = []
            for v in vowels:
                for v2 in allPossibleMelodius(n-1, False):
                    result.append(v + v2)
            return result
    else:
        if n <= 1:
            return list(consonants)
        else:
            result = []
            for c in consonants:
                for c2 in allPossibleMelodius(n-1, True):
                    result.append(c + c2)
            return result


n = int(str(input()).strip())

arr = allPossibleMelodius(n,True) + allPossibleMelodius(n,False)

for s in arr:
    print(s)
