---
title: 快速排列
date: 2016-10-11 23:59:02
categories:
tags:
---
利用位运算，快速实现排列。
<!-- more -->
<!-- toc -->

## 深度搜索
利用递归，每一次放置，首先检查其是否与前面的数重合。
``` cpp
#include <iostream>
#include <ctime>
#include <string>
static int n, end, count = 0;
static int *sol = new int [n] {};
void print() {
    for(int i =0; i < n; ++i) std::cout << sol[i];
    std::cout << ";" << count << "\n";
}
void permutation( int pos ) {
    for(int i = 0; i < n; ++i) {
        bool ok = true;
        for(int j =0; j < pos; ++j) {
            if(i == sol[j]) {
                ok = false;
                break;
            }
        }
        if( ok ) {
            if(pos == end) {
                count++;
                //print();
            }
            else {
                sol[pos] = i;
                permutation(pos+1);
            }
        }
    }
}

int main(int argc, char const *argv[]) {
    n = std::stoi(argv[1]);
    if( argc == 3)
        end = std::stoi(argv[2]) - 1;
    else
        end = n - 1;
    std::clock_t tic = std::clock();
    permutation(0);
    std::clock_t toc = std::clock();
    std::cout << "Solution: " << count << " " << float(toc - tic) / CLOCKS_PER_SEC << "s\n";
    return 0;
}
```

## 优化深度搜索
利用一个数组来标记哪些数已经被占用了：
``` cpp
static int n, end, count = 0;
static bool *avai = new bool [n] {};
void permutation( int pos ) {
    for(int i = 0; i < n; ++i) {
        if( !avai[i] ) {
            if (pos == end) {
                count++;
            }
            else {
                avai[i] = true;
                permutation(pos+1);
                avai[i] = false;
            }
        }
    }
}
```

## 位优化
利用位来标记哪些数已经被占用了：
``` cpp
static int n, end, count = 0;
static int avai = 0;
void permutation( int pos ) {
    for(int i = 0; i < n; ++i) {
        if( ( avai & (1<<i) ) == 0 ) {
            if (pos == end) {
                count++;
            }
            else {
                avai ^= (1<<i);
                permutation(pos+1);
                avai ^= (1<<i);
            }
        }
    }
}
```

## 快速位
利用位来标记哪些数已经被占用了，并且每一次迭代直接取出未占用的数：
`x & -x`可以取出最右边为1的那一位。
``` cpp
static int n, end, count = 0, avai = 0;
void permutation( int pos ) {
    int empty =  ((1<<n)-1) & ~avai; // acquire the available bits and set them to 1.(eg 01110110)
    while( empty != 0 ) {
        int p = empty & (-empty);//pick the most right bit that equals 1.(eg 00000010)
        empty ^= p; //set this bit to be 0, which means occupied. (eg 01110100)
        if (pos == end) {
            count++;
        }
        else {
            avai ^= p;
            permutation(pos+1);
            avai ^= p;
        }
    }
}
```

## 更多优化
增加函数参数，减少运算量：
``` cpp
static int n, end, count = 0;
void permutation( int pos, int avai ) {
    int empty =  ((1<<n)-1) & ~avai;
    while( empty != 0 ) {
        int p = empty & (-empty);
        empty ^= p;
        if (pos == end) {
            count++;
        }
        else  {
            permutation(pos+1, avai^p);
        }
    }
}
```


## Codes
[Download](/exam/fast-permutation.tgz)
[GitHub](https://github.com/sheng09/sheng09.github.io.posts/tree/master/_posts/fast-permutation)
