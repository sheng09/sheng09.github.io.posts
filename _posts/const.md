---
title: Const in C/C++
date: 2017-01-21 17:07:40
categories: [Programming]
tags: [c++]
---

## Const Associated

Associating pointers, 
``` c++
int x = 10, y = 20;

int * const p1 = &x; // p1 is a top-level const, p1 cannot be changed, but not the object it points
const int  *p2 = &x; // p2 is a low-level const, the object pointed by p2 cannot be changed, but not p2
int const  *p3 = &x; // equal to "const int"
const int *const p4 = &x; // neither p4 nor the object pointed by p4 can be changed

*p1 = 0;
p1 = &y; // wrong
*p2 = 0; // wrong
p2 = &y;
```

The pointer that points to a const object must be a low-level const
``` c++
const int x = 99;
int y = 88;
int *p1 = &x; // wrong
const int *p2 = &x; // correct
*p2 = 80;     // wrong
p2 = &y;      // correct
```
