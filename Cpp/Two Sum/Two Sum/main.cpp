//
//  main.cpp
//  Two Sum
//
//  Created by Bo Zhou on 11/8/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <vector>
#include "Solution.cpp"
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    int target = 9;
    vector<int> nums;
    nums.push_back(2); nums.push_back(7); nums.push_back(11); nums.push_back(15);
    
    Solution f;
    vector<int> ans = f.twoSum(nums, target);
    
    for (auto i = ans.begin(); i != ans.end(); ++i)
        std::cout << *i << ' ';
    
}
