# dynamic programming for coin change

def change(amount, coins):
    combinations = [0] * (amount+1)
    combinations[0] = 1

    for coin in coins:
        i = 1
        while i < len(combinations):
            if i >= coin:
                combinations[i] += combinations[i-coin]
            i += 1

    return combinations[amount]


amount = 12
coins = [1,2,5]
c = change(amount, coins)
print(c)
