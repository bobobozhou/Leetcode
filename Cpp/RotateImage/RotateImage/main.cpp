//
//  main.cpp
//  RotateImage
//
//  Created by Bo Zhou on 11/13/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <vector>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {
    
    // construct a matrix for input
    const int M=3, N=3;
    int matrix[M][N] = {1,2,3,4,5,6,7,8,9};
    vector<vector<int>> Mat(M,vector<int>(N,0));
    
    for (int i=0; i<M; i++) {
        for (int j=0; j<N; j++) {
            Mat[i][j] = matrix[i][j];
        }
    }
    
    Solution f;
    f.rotate(Mat);

    cout << 1 << endl;
};
