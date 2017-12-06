//
//  Solution.hpp
//  ImageSmoother
//
//  Created by Bo Zhou on 11/15/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#ifndef Solution_hpp
#define Solution_hpp

#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    
    vector<vector<int>> imageSmoother(vector<vector<int>> &M) {
        
        int l_row = (int)M.size();
        int l_col = (int)M[0].size();
        vector<vector<int>> ans(l_row, vector<int>(l_col, 1));
        
        for (int i=0; i<l_row; i++) {
            for (int j=0; j<l_col; j++) {
                int val = 0;
                int size = 0;
                
                for (int ni = i-1; ni < i+2; ni++) {
                    for (int nj = j-1; nj < j+2; nj++) {
                        
                        if (0<=ni && ni<l_row && 0<=nj && nj<l_col) {
                            val = val + M[ni][nj];
                            size = size + 1;
                        };
                        
                    };
                };
                
                ans[i][j] = val/size;
                
            };
        };
        
        return ans;
        
    };
    
};


#endif /* Solution_hpp */
