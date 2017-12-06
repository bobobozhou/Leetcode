//
//  Solution.hpp
//  RomantoInteger
//
//  Created by Bo Zhou on 11/13/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <string>
#include <unordered_map>
using namespace std;

class Solution{
public:
    int romanToInt(string s) {
        
        unordered_map<char, int> d = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        
        int sum = d[s.back()];
        
        for (int i = s.length()-2; i>=0; i--) {
            if (d[s[i]] < d[s[i+1]]) {
                sum -= d[s[i]];
            }
            else {
                sum += d[s[i]];
            }
        }
        
        return sum;
        
    }
    
};

#endif /* Solution_hpp */
