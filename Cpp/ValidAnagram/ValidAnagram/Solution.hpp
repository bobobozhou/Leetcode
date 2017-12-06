//
//  Solution.hpp
//  ValidAnagram
//
//  Created by Bo Zhou on 11/14/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    
    bool isAnagram(string s, string t) {
        
        if (s.length() != t.length()) {
            return false;
        };
        
        unordered_map<char, int> C;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            C[s[i]] += 1;
            C[t[i]] -= 1;
        };
        
        for (auto c : C) {
            if (c.second != 0) return false;
        };
        
        return true;
    };
    
};

#endif /* Solution_hpp */
