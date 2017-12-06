//
//  main.cpp
//  ValidPerfectSquare
//
//  Created by Bo Zhou on 11/14/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {
    
    Solution f;
    
    int Num = 100;
    
    bool res = f.isPerfetSquare(Num);
    
    cout<<boolalpha<<res<<endl;
    
}
