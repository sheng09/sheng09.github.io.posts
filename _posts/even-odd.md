---
title: 位运算--快速判断奇偶性
date: 2016-10-10 09:03:10
categories: [programming]
tags: [bit, algorithm, programming]
---

利用位运算，可以快速的判断整数的奇偶性。
整数位存储时，最低位如果是0，那么对应于偶数，如果是1，则对应于奇数。（注意负数的补码）
代码如下：

``` cpp
#define ISODD(x) ((x)&1)
```

测试：
```cpp
//test.cpp
#define ISODD(x) ((x)&1)
#include <iostream>
int main(int argc, char** argv) {
  int    x[5] = {0, 10, 11, -10, -13};
  long   l[4] = {10, 11, -10, -13};
  short  s[4] = {10, 11, -120, -17};
  for(int i = 0; i < 5; ++i) {
    if( ISODD(x[i]) )
      std::cout << "int:" << x[i] << ": odd\n";
    else
      std::cout << "int:" << x[i] << ": even\n";
  }
  for(int i = 0; i < 4; ++i) {
    if( ISODD(l[i]) )
      std::cout << "long:" << l[i] << ": odd\n";
    else
      std::cout << "long:" << l[i] << ": even\n";
  }
  for(int i = 0; i < 4; ++i) {
    if( ISODD(s[i]) )
      std::cout << "short:" << s[i] << ": odd\n";
    else
      std::cout << "short:" << s[i] << ": even\n";
  }
}
```

运行：
``` bash
bash> g++ test.cpp -o test  #compile
bash> ./test
int:0: even
int:10: even
int:11: odd
int:-10: even
int:-13: odd
long:10: even
long:11: odd
long:-10: even
long:-13: odd
short:10: even
short:11: odd
short:-120: even
short:-17: odd
base>
```
