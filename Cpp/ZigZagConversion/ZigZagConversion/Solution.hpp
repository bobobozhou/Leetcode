//
//  Solution.hpp
//  ZigZagConversion
//
//  Created by Bo Zhou on 11/15/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <iostream>
#include <ostream>
#include <string>
using namespace std;

class Solution {
public:
    
    string convert(string s, int numRows) {
        
        if (numRows <= 1) return s;
        
        const int len = (int)s.length();
        string *str = new string[numRows];  //what happens here?
        int step = 1;
        int row = 0;
        
        for (int i = 0; i < len; i++) {
            
            str[row].push_back(s[i]);
            
            if (row == 0) {
                step = 1;
            } else if (row == numRows - 1) {
                step = -1;
            };
            
            row = row + step;
            
        };
        
        string res;
        for (int j = 0; j < numRows; j++) {
            res.append(str[j]);
        };
        
        return res;
        
    };
    
};


#endif /* Solution_hpp */
