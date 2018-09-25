# Word Order Challange
# Written by: Cameron Napoli
# Problem found at:
#   https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

n = int(raw_input())

word_ord_dict = OrderedDict()

for i in range(n):
    word = str(raw_input())

    if word in word_ord_dict:
        word_ord_dict[word] += 1
    else:
        word_ord_dict[word] = 1

print( len(word_ord_dict.keys()) )
print( ' '.join(map(lambda x: str(x), word_ord_dict.values())) )
