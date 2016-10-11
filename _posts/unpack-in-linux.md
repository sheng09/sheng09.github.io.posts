---
title: 怎么在linux下压缩和解压文件
date: 2016-06-09 00:34:36
categories: [Linux工具及配置]
tags: [Linux]
---

此文是写给呆萌女朋友的。
<!-- more -->

<!-- toc -->


## tar.gz
1.使用tar打包并压缩文件(夹)
``` bash
$ tar -cvzf  test.tar.gz  test
```
可以将test打包压缩并生产test.tar.gz，test可以是文件夹也可以是文件。
切记，被压缩文件与压缩输出文件不要写反了，否则被压缩文件会被覆盖从而丢失！

2.解包并解压 .tar.gz
``` bash
$ tar -xvzf  test.tar.gz
```

## tar.bz2
1.使用tar打包并压缩文件(夹)
``` bash
$ tar -cjzf  test.tar.bz2  test
```
可以将test打包压缩并生产test.tar.bz，test可以是文件夹也可以是文件。

2.解包并解压 .tar.bz
``` bash
$ tar -xjzf  test.tar.bz2
```

## zip
1.使用zip压缩
``` bash
$ zip  -r  test.zip   test
```
将test打包压缩并生产test.zip，test可以是文件夹也可以是文件；

2.解压zip
``` bash
$ unzip   test.zip
```

## rar
最好不要用rar，rar压缩算法不是开源的，所以linux中默认可能没有处理rar的工具。倘若强行需求，可以先安装rar
ubuntu中安装命令如下：
``` bash
$ sudo apt-get install rar
```

1.使用rar压缩文件或文件夹
``` bash
$ rar  a  test.rar  test
```
可以将test打包压缩并生产test.rar，test可以是文件夹也可以是文件；

2.解压rar
``` bash
$ rar  x  test.rar
```

## 后缀名说明
一般情况，可以通过后缀名来判断需要用什么软件来解压。.tar.gz 或者.tgz的后缀都是用tar操作的。 而.zip后缀名显然是zip操作的。 .rar后缀名显然是rar操作的
自己打包压缩文件时候，一定要写后缀名，其他人看到后缀名就可以知道应该用那个解压工具。
