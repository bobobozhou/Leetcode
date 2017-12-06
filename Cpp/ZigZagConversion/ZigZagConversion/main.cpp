//
//  main.cpp
//  ZigZagConversion
//
//  Created by Bo Zhou on 11/15/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include "Solution.hpp"
#include <string>
using namespace std;

int main(int argc, const char * argv[]) {
    
    string s = "ABCD";
    int numRows = 3;
    Solution f;
    
    string res = f.convert(s, numRows);
    
    cout << res << endl;
    
}
