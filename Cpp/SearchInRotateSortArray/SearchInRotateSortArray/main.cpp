//
//  main.cpp
//  SearchInRotateSortArray
//
//  Created by Bo Zhou on 11/16/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <vector>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {
    
    vector<int> nums = {3,1};
    
    Solution f;
    int tar = 3;
    int res_ind = f.search(nums, tar);
    
    cout<<res_ind<<endl;
    
}
