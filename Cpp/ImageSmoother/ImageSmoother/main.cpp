//
//  main.cpp
//  ImageSmoother
//
//  Created by Bo Zhou on 11/15/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <vector>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {
    
    vector<vector<int>> M = {{1,1,1,1,1}, {1,1,1,1,1}, {1,1,100,1,1}, {1,1,1,1,1}, {1,1,1,1,1}};
    
    Solution f;
    
    vector<vector<int>> ans = f.imageSmoother(M);
    
    int a = 1;
    
};
