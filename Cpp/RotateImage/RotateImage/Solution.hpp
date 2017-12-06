//
//  Solution.hpp
//  RotateImage
//
//  Created by Bo Zhou on 11/13/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>> &matrix) {
        reverse(matrix.begin(), matrix.end());
        for (int i=0; i<matrix.size(); ++i) {
            for (int j=i+1; j<matrix[i].size(); ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    };
};

#endif /* Solution_hpp */
