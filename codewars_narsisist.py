def narcissistic(value):
    sum = 0
    for digit in list(map(lambda x: int(x), str(value))):
        sum += digit ** len(str(value))
    return sum == value

print(narcissistic(153)) # 1^3 + 5^3 + 3^3  = 153
print(narcissistic(154)) # 1^3 + 5^4 + 4^3 != 154
