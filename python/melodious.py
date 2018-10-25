# Written by: Cameron Napoli
# Problem found on hackerrank.com at:
#     https://www.hackerrank.com/contests/w30/challenges/melodious-password


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
