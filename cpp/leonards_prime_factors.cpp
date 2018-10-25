// Written by: Cameron Napoli
// Problem found on hackerrank.com at:
//     https://www.hackerrank.com/challenges/leonardo-and-prime/problem

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
