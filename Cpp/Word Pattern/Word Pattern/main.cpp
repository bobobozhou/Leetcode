//
//  main.cpp
//  Word Pattern
//
//  Created by Bo Zhou on 11/5/17.
//  Copyright © 2017 CMU. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include "Solution.hpp"
using namespace std;

int main(int argc, const char * argv[]) {
    
    string a = "abba";
    string b = "dog cat cat dog";
    
    Solution f;
    bool p = f.wordPattern(a, b);
    
    std::cout << boolalpha << p << endl;
    
};

