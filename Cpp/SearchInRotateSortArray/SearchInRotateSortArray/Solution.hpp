//
//  Solution.hpp
//  SearchInRotateSortArray
//
//  Created by Bo Zhou on 11/16/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <istream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

class Solution {
public:
    
    int search(vector<int> &nums, int target) {
        
        int lo = 0;
        int hi = nums.size();
        
        while (lo < hi) {
            int mid = (lo + hi)/2;
            
            long num = (nums[mid] < nums[0]) == (target < nums[0])
            ? nums[mid]
            : target < nums[0] ? -INFINITY : INFINITY;
            
            if (num > target) {
                hi = mid;
            } else if (num < target) {
                lo = mid + 1;
            } else {
                return mid;
            }
            
        };
        
        return -1;
        
    };
    
};

#endif /* Solution_hpp */
