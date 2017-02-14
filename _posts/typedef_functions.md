---
title: "typedef" for functions
date: 2015-01-20 21:37:45
categories: Programming
tags: [c++]
---

`typedef` is powerful in simplifing complex declaration, expesically for function pointer type declaration.

``` c++
/* test 
 * g++ test.cxx -o test
 */

#include <iostream>
typedef int (*pCAL)(int x, int y); // function pointer
typedef int CAL(int x, int y);     // function

int add(int x, int y) {return x+y;}
int mul(int x, int y) {return x*y;}

int main(int argc, char *argv[]) {
    pCAL pproc1 = add;
    pCAL pproc2 = mul;
    CAL  *proc1 = add;
    CAL  *proc2 = mul;
    std::cout<< pproc1(3, 4) << "\n";
    std::cout<< pproc2(3, 4) << "\n";
    std::cout<< proc1(3, 4) << "\n";
    std::cout<< proc2(3, 4) << "\n";
    return 0;
}
```


