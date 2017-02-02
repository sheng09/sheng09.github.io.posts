---
title: Const in C/C++
date: 2015-01-31 17:07:40
categories: [Programming]
tags: [c++]
---

This post introduces usage of "const", especially terms of "top-level const" and "low-level const".

<!--more-->
<!--toc-->

## Const Associated
Associating pointers, `const` is used to declare that pointer is a const, or the object pointed by it is a const. This difference leads to "top-level const" and "low-level const".
``` c++
// top-level const and low-level const
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

## Const in Formal Parameter

In functions, declaring a formal parameter as const follows the principle of using const for variables. The top-level const is ignored whether it is in formal or actual parameters.
``` c++
// top-level const in actual parameter
void fun1(int i) {}
void fun2(int* p) {}

const int x = 0;
int y = 0;
int *const p = &y;
fun1(x); // correct, it is like "int tmp = x", so whether tmp should be const or not doesn't matter
fun2(p); // correct, it is like "int *tmp = p", 
```

``` c++
//top-level const in formal parameter
void fun1(const int i) {}
void fun2(int *const p) {}

int x = 0;
int *p = &x;
fun1(x); // correct
fun2(p); // correct it is like "int *const tmp = p", whether p is const or not doesn't matter
```
## In Template
Principles described above apply to template as well.

``` c++
// template
template <class T> T f(T, T);
int x;
const int y;
f(x,y); // call f(int, int); const is ignored
```



