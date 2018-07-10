# Written by: Cameron Napoli
# Problem found at:
#     https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import sys

def rotateLetter(l, k):
    '''
    Rotate's a letter using a Caesar cypher using the key k

    :param l: letter to be rotated
    :param k: key indicating how much to rotate the letter
    :returns: rotated letter
    '''

    # First, make sure the letter is a valid lowercase letter
    if ord(l.lower()) < 123 and ord(l.lower()) > 96:

        # extract integer value of letter and add the keys value to it
        letterVal = ord(l.lower()) + (k % 26)

        # if value exceeds z return it to value
        if letterVal > 122:
            letterVal -= 26

        # return the letter converted back from integer form
        return chr(letterVal) if not (l != l.lower()) else chr(letterVal-32) # return to original value if is upper
    return l

def caesarCypher(s, k):
    return ''.join([rotateLetter(letter,k) for letter in s])

n = int( str(input()).strip() )
s = str(input()).strip()
k = int( str(input()).strip() )
