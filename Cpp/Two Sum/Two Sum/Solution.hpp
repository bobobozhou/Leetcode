//
//  Solution.hpp
//  Two Sum
//
//  Created by Bo Zhou on 11/8/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> res;
        unordered_map<int, int> m;

        for (int i=0;i<nums.size();i++) {
            int numToFind = target - nums[i];

            if (m.find(numToFind) != m.end()) {
                res.push_back(m[numToFind]);
                res.push_back(i);
                return res;
            }

            m[nums[i]] = i;

        };

        return res;
    };
    
};
#endif /* Solution_hpp */
