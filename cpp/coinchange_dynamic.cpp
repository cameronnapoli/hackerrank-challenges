// dynamic programming for coin change
#include <iostream>

int change(int amount, int coins[], int coins_len) {
    int combinations[amount+1];
    for(int i = 0; i < amount+1; i++){
        combinations[i] = 0;
    }
    combinations[0] = 1;

    for(int i = 0; i < coins_len; i++) {
        int coin = coins[i];
        for(int j = 0; j < amount+1; j++) {
            if (j >= coin) {
                combinations[j] += combinations[j-coin];
            }
        }
    }

    return combinations[amount];
}

int main() {
    int amount = 12;
    int coins[] = {1,2,5};
    std::cout << change(amount, coins, 3) << "\n";
    return 0;
}
