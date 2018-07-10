# Written by: Cameron Napoli
# Problem found at:
#     https://www.hackerrank.com/challenges/sherlock-and-array/problem

from functools import reduce

def satisfiedCond(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    if len(arr) == 2:
        return False
    i = 1
    sum_left = arr[0]
    sum_right = reduce(lambda x,y:x+y, arr[i+1:])
    while(i < len(arr)-1):
        if(sum_left == sum_right):
            return True
        sum_left += arr[i]
        sum_right -= arr[i+1]
        i += 1
    return False

n = input()
for line in range(int(n)):
    length = input()
    arr = list(map(lambda x: int(x), input().split(" ")))
    if satisfiedCond(arr):
        print("YES")
    else:
        print("NO")
