# Watson gives Sherlock an array  of length . Then he asks him to determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero.
# Formally, find an , such that, .
#
# Input Format
#
# The first line contains , the number of test cases. For each test case, the first line contains , the number of elements in the array . The second line for each test case contains  space-separated integers, denoting the array .
#
# Constraints
#
#
#
#
# Output Format
#
# For each test case print YES if there exists an element in the array, such that the sum of the elements on its left is equal to the sum of the elements on its right; otherwise print NO.
#
# Sample Input 0
#
# 2
# 3
# 1 2 3
# 4
# 1 2 3 3
#
# Sample Output 0
#
# NO
# YES

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
