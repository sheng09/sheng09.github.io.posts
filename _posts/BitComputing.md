---
title: 位运算
date: 2016-10-07 05:17:17
categories: [programming]
tags: [bit, programming]
---

1个Byte由8个Bit构成，每一个Bit为0或1。针对这一特性，利用位来存储数据，可以实现空间最优化。此外，由于CPU指令集可以一次性操作多个Bit，故这一方法可以避免对数据元素的循环遍历操作，从而实现加速。

<!--more-->

<!-- toc -->


## 位
针对某一数据，获取其位数据可以使用以下函数`getBits()`：
``` cpp
//getBits.cpp
//Compile: g++ getBits.cpp -c -std=c++11 -o getBits
#include <iostream>
#include <string>
template <typename T> std::string getBits(T _x)
{
  long len   = sizeof(T) * 8 - 1;
  std::string str = '[' + std::to_string(len+1) + "bits]";
  long x = *( (long*)(&_x) );
  while( len-- != 0 ) {
    if( (x >> len) & 1 )
      str+= '1';
    else
      str+= '0';
  }
  return str;
}
```

## 位操作

#### 位逻辑运算`& | ~ ^`
不同于逻辑运算符中的“与”“或”“非”“亦或”，位逻辑运算并不对数据的“TRUE”或“FALSE”，而是针对每一位的“0”或“1”做逻辑操作。例如：

```
00010100 & 00001100 = 00000100
00010100 | 00001100 = 00000100
00010100 ^ 00001100 = 00011000
~00000010 = 11111101
```
#### 移位运算 `<<` `>>`
`<<` `>>`分别表示将数据位整体左移和右移。例如：
```
(00000001 << 2) = 00000100
(00001000 >> 3) = 00000001
```
值得注意的是，右移运算符号涉及到符号位移动的处理，分为逻辑移位与算术移位。不同数据的具体实现方式，请参考对应标准。

#### bit mask
构建一个值A，其某些位为0，某些位为1。那么将数据与A做位运算可以实现对数据特定位的修改。

提取数据的第1位： `dat & 00000010`;
设置数据第3位为0: `dat &= 11110111 `;
设置数据第3位为1：`dat |= 00001000 `;
数据第3位取反：`dat ^= 00001000 `;
提取数据最右边为1的那一位：`dat & -dat`;

``` cpp
//Test
int main(int argc, char const *argv[]) {
  char a = 95;
  char index = 1;
  std::cout << "a:" << getBits(a) << "\n";
  std::cout << "a & 00000001:" << getBits( (char)( a & index   ) ) << "\n";
  std::cout << "a & 11111110:" << getBits( (char)( a & (~index)) ) << "\n";
  std::cout << "a | 00000001:" << getBits( (char)( a | index   ) ) << "\n";
  std::cout << "a ^ a       :" << getBits( (char)( a ^ a   ) ) << "\n";
  std::cout << "a &-a       :" << getBits( (char)( a &-a   ) ) << "\n";

  a = 90;
  std::cout << "a:" << getBits(a) << "\n";
  std::cout << "a & 00000001:" << getBits( (char)( a & index   ) ) << "\n";
  std::cout << "a & 11111110:" << getBits( (char)( a & (~index)) ) << "\n";
  std::cout << "a | 00000001:" << getBits( (char)( a | index   ) ) << "\n";
  std::cout << "a ^ a       :" << getBits( (char)( a ^ a   ) ) << "\n";
  std::cout << "a &-a       :" << getBits( (char)( a &-a   ) ) << "\n";
  return 0;
}
```
