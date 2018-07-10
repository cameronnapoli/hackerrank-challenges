// Written by: Cameron Napoli
// Problem found on hackerrank.com at:
//     https://www.hackerrank.com/challenges/migratory-birds/problem

#include <iostream>
#include <map>

std::map<int, int> build_freq_map(int n) {
    // Build map with keys and frequencies
    std::map<int, int> m;
    int id;
    for (int i = 0; i < n; i++) {
        std::cin >> id;
        if (m.find(id) != m.end()) { m[id]++; }
        else { m[id] = 1; }
    } return m;
}

int main() {
    int n; std::cin >> n;

    std::map<int, int> m = build_freq_map(n);

    int max_freq_key = 0; int max_freq = 0;
    for (const auto& kv : m) {
        int key  = kv.first;
        int freq = kv.second;

        if (freq > max_freq) {
            max_freq_key = key;
            max_freq = freq;
        } else if (freq == max_freq && key < max_freq_key) {
            max_freq_key = key;
            max_freq = freq;
        }
    }

    std::cout << max_freq_key << std::endl;
    return 0;
}
