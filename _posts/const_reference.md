---
title: Const Reference in Function Parameters
date: 2016-06-09 16:07:40
categories: [programming]
tags: [c++]
---

<!-- toc -->

This post presents tips of using `const reference` in functions. Examples are presented for wrong using.

## In Function Parameters
`reference` is used to declare the formal parameters in a function, in order to speed up programs. However, a `const` argument may be 
passed into this function, then compiling fails. This is because "constructing a `reference` to a const variable" is wrong. The resolution 
is "construting a `const reference` to a const variable", or "construting a `const reference` to a whatever variable".

eg:
``` c++
void foo(int & v) {}
int v1 = 1;
const int v2 = 2;
foo(v1);   // correct
foo(v2);   // wrong, passing "const int" to "int &"
foo(3);    // wrong

void foo2(const int & v) {}
foo2(v1);   // correct
foo2(v2);   // correct
foo2(3);    // correct

int& foo3(const int & v) {return v;} //false, passing "const int&" to "int&" in return
const int& foo3(const int & v) {return v;} //correct
```

## In Class Methods
When calling a method for a class instance through its `const reference`, this method should be declared to be `const`.

In example below, compiler fails and error message is `passing "const XX" as this argument of "void XX::XX()" discards qualifiers`. 
This is because a non-const methods `dosth()` is called on a const object `rt`. In other words, a const `rt` is passing 
into  non-const parameter in `TEST::dosth()`. 
``` c++
class TEST {
public:
    TEST() {};
    ~TEST() {};
  
  void dosth() {}           // fail
  //void dosth() const {}   // using this 
};

int main() {
    TEST t;
    const TEST &rt = t;
    rt.dosth();
    return 0;
}
```

## Conclusions and Tips
- Use `const reference` in formal parameters if `reference` is required.
- Once using `const reference` in formal parameters, any operations to it should be const!
- Use pointer but not reference if you want to pass a big data set, 
such as a struct instance, into a function, and you will change it.

``` c++
// tip 1
void fun(const int & v); // use const reference, don't change v 

// tip 2
class TEST {/*...*/};  
void fun(const TEST & t); // do not call non-const method for t in fun()

// tip 3
class DAT {/*...*/};
void pro(DAT *d); // use pointer if changes is made to d in pro()
```
