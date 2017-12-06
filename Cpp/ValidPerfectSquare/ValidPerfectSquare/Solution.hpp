//
//  Solution.hpp
//  ValidPerfectSquare
//
//  Created by Bo Zhou on 11/14/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <iostream>
using namespace std;

class Solution {
public:
    
    bool isPerfetSquare(int num) {
        
        long high = num;
        long low = 0;
        
        while (high > low) {
            long mid = (high + low)/2;
            
            if (mid*mid > num) {
                high = mid;
            } else if (mid*mid < num) {
                low = mid+1;
            } else {
                return true;
            }
        };
        
        return low*low == num;
        
    };
    
};

#endif /* Solution_hpp */
