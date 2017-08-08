# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
#
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.
#
# Example:
#
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# Have fun coding it and please don't forget to vote and rank this kata! :-)
#
# I have also created other katas. Take a look if you enjoyed this kata!


# finds the missing letter in increasing order in an array
def find_missing_letter(chars):
    current = ord(chars[0])
    for c in chars[1:]:
        if ord(c) != (current+1):
            return chr(current+1)
        current = ord(c)

print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))
