//
//  main.cpp
//  RomantoInteger
//
//  Created by Bo Zhou on 11/13/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <string>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {

    string a = "IVXM";
    Solution f;
    int res = f.romanToInt(a);
    
    cout << res << endl;
    
}
