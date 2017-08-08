# Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, , making it unreadable by his enemies. Given a string, , and a number, , encrypt  and print the resulting string.
#
# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
#
# Input Format
#
# The first line contains an integer, , which is the length of the unencrypted string.
# The second line contains the unencrypted string, .
# The third line contains the integer encryption key, , which is the number of letters to rotate.
#
# Constraints
#
#
#  is a valid ASCII string and doesn't contain any spaces.
#
# Sample Input:
#
# 11
# middle-Outz
# 2
#
# Sample Output:
#
# okffng-Qwvb

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
