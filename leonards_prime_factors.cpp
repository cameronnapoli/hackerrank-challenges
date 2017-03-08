/*
Leonardo loves primes and created  queries where each query takes the form of an integer, . For each , he wants you to count the maximum number of unique prime factors of any number in the inclusive range  and then print this value on a new line.

Note: Recall that a prime number is only divisible by  and itself, and  is not a prime number.

Input Format

The first line contains an integer, , denoting the number of queries.
Each line  of the  subsequent lines contains a single integer, .

Constraints



Output Format

For each query, print the maximum number of unique prime factors for any number in the inclusive range  on a new line.
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    int primes[17] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59};
    for(int i = 0; i < n; i++) {
        unsigned long long int inp;
        cin >> inp;
        if(inp <= 1) {
            cout << 0 << "\n";
        } else {
            unsigned long long int primeProduct = 1;
            for(int pIndex = 0; pIndex < 17; pIndex++) {
                primeProduct *= primes[pIndex];
                if(primeProduct > inp) {
                    cout << pIndex << "\n";
                    break;
                }
            }
        }
    }
    return 0;
}
