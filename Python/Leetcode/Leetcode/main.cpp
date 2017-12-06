//
//  main.cpp
//  Leetcode
//
//  Created by Bo Zhou on 11/5/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}



bool wordPattern(string pattern, string str) {
    unordered_map<char, int> m1;
    unordered_map<string, int> m2;
    istringstream in(str);
    int i = 0;
    for (string word; in >> word; ++i) {
        if (m1.find(pattern[i]) != m1.end() || m2.find(word) != m2.end()) {
            if (m1[pattern[i]] != m2[word]) return false;
        } else {
            m1[pattern[i]] = m2[word] = i + 1;
        }
    }
    return i == pattern.size();
}
