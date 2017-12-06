//
//  main.cpp
//  ValidAnagram
//
//  Created by Bo Zhou on 11/14/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    string s = "anagram";
    string t = "nangram";
    
    Solution f;
    bool res = f.isAnagram(s, t);
    
    cout<<boolalpha<<res<<endl;
    
}
