---
title: 利用总控Makefile一次性编译所有子程序包
date: 2016-06-09 16:07:40
categories: [Programming]
tags: [Makefile,Linux,Compiling, Programming]
---

当一个大的项目由很多子程序组成，而每一个子程序包都有自己独立的`Makefile`，这时候就需要一个`总控Makefile`来一次性完成所有的编译工作。以下给出了一个例子，以说明如何构建`总控Makefile`。
<!-- more -->
## 文件结构
项目[PRJ](/exam/PRJ.tgz)包含了三个子程序包。每个子程序包都拥有自己的`Makefile`，从而可以在各目录下使用`Make`完成编译。但是这样很麻烦。通过构建总控`Makefile`(`PRJ/Makefile`)，可以一次性编译`prj_sub1`,`prj_sub2`,`prj_sub3`三个子程序包。
``` bash
PRJ/
├── prj_sub1/
│   ├── a.c
│   ├── b.c
│   ├── c.c
│   └── Makefile
|
├── prj_sub2/
│   ├── d.c
│   ├── e.c
│   └── Makefile
├── prj_sub3/
│   ├── f.c
│   ├── g.c
│   └── Makefile
├── ...
└── Makefile
```

## 子程序包Makfile
子程序包中的`Makefile`包含了`编译`,`install`,`clean`操作。以下例子中，有关函数`foreach`,自动化变量`$@ $<`,以及`静态模式`的内容可以参见[X](X)。
需要注意的是变量`BIN`并没有在`Makefile`中声明赋值，而是通过`总控Makefile`中的`export`来传递。
``` bash
#Makefile for prj_sub1/
CC = gcc
EXEC = a b c
OBJ  = $(foreach exe, ${EXEC}, ${exe}.o)

all: ${OBJ} ${EXEC}

${EXEC}:%:%.o
	${CC} -o $@ $<

${OBJ}:%.o:%.c
	${CC} -c -o $@ $<

install:
	cp ${EXEC} ${BIN}

clean:
	rm ${EXEC} ${OBJ}
```

## 总控Makefile

``` bash
export BIN=../bin

SUBS = prj_sub1 prj_sub2 prj_sub3
SUBS_make    = $(foreach sub, ${SUBS}, ${sub}.make)
SUBS_clean   = $(foreach sub, ${SUBS}, ${sub}.clean)
SUBS_install = $(foreach sub, ${SUBS}, ${sub}.install)

all: ${SUBS_make}

${SUBS_make}:%.make:%
	make -C $<

install: ${SUBS_install}

${SUBS_install}:%.install:%
	-make -C $< install

clean: ${SUBS_clean}

${SUBS_clean}:%.clean:%
	-make -C $< clean
```
总控Makefile一次性编译了`prj_sub1`,`prj_sub2`,`prj_sub3`三个子程序包。
首先对变量`SUBS_make`赋值，为`prj_sub1.make prj_sub2.make prj_sub3.make`。类似的，完成变量`SUBS_clean`，`SUBS_install`的赋值。
随后，在编译中，`${SUBS_make}:%.make:%`声明从变量`SUBS_make`中逐次提取以`.make`结尾的字段作为编译目标，去掉
`.make`之后的内容作为编译依赖项目，进而利用`make -C $<`完成编译。第10,11行等价于：

``` bash
prj_sub1.make: prj_sub1
	make -C prj_sub1

prj_sub2.make: prj_sub2
	make -C prj_sub2

prj_sub3.make: prj_sub3
	make -C prj_sub3

```
`make -C prj_sub1`等价于`cd prj_sub1; make`。其相当于先进入目录`prj_sub1`，然后执行`make`命令。
与编译类似，`install`与`clean`操作一次性完成所有子程序包的安装及清理操作。
需要注意的是，利用`export BIN=../bin`，将变量`BIN`传递至被调用`Makefile`。
