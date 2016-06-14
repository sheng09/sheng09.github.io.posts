---
title: Linux终端美化
date: 2016-06-08 23:29:05
categories: [Linux工具及配置]
tags: [Linux, Terminal]
---

不知道你是不是受够了Linux终端的丑陋。黑色衬底配上刺眼的颜色和奇怪的字体，是默认Linux的终端外观。如果你长期需要在Linux下作业，那么一个养眼的终端带来的将是身心愉悦，效率翻倍，毕竟这是一个凡事看脸的时代，颜即正义。

<!-- more -->
<!-- toc -->
## 配色方案
默认配色大多指向16位色彩方案，在带给新人一种geek的感觉之后，时刻冲击着用户视觉神经。那么来试试[`dircolors-solarized`](https://github.com/seebi/dircolors-solarized)吧。
![](/img/screen-dircolors-in-iTerm2-solarized_dark.png)

在[`dircolors-solarized`](https://github.com/seebi/dircolors-solarized)项目主页下载配色方案。解压后可以发现文件夹内包含了不同的配色设置文件，以其中的`dircolors.ansi-dark`为例，在`~/.basrc`(或者`~/.profile`)中添加以下内容：

``` bash
eval `dircolors /path/to/your/dircolors.ansi-dark`
```
在终端中`source`一下，或者关闭重启以下终端，配色是不是变了？

## 提示符
在终端里，默认的提示符包含了当前路径及用户登陆信息，臃肿而又难看。试试再`~/.basrc`(或者`~/.profile`)中添加以下内容：
``` bash
PS1='`a=$?;if [ $a -ne 0 ]; then a="  "$a; echo -ne "\[\e[s\e[1A\e[$((COLUMNS-2))G\e[31m\e[0;41m${a:(-3)}\e[u\]\[\e[0m\e[7m\e[2m\]"; fi`\[\e[1;35m\]Fa\[\e[1;33m\]nc\[\e[1;32m\]y \[\e[0m\e[1;36m\]\u \[\e[0;34m\]\$ \[\e[0m\]'
```
在终端中`source`一下，或者关闭重启以下终端，看一看新的提示符。
以`\[\e[1;35m\]Fa`为例，字段，字段`1;35`分别声明了`Fa`的颜色与字体方案。
除了使用类似于`Fa`的普通文本内容，还有以下特殊符号：
　　`\d` :代表日期，格式为weekday month date，例如："Mon Aug 1"
　　`\H` :完整的主机名称。例如：我的机器名称为：fc4.linux，则这个名称就是fc4.linux
　　`\h` :仅取主机的第一个名字，如上例，则为fc4，.linux则被省略
　　`\t` :显示时间为24小时格式，如：HH：MM：SS
　　`\T` :显示时间为12小时格式
　　`\A` :显示时间为24小时格式：HH：MM
　　`\u` :当前用户的账号名称
　　`\v` :BASH的版本信息
　　`\w` :完整的工作目录名称。家目录会以 ~代替
　　`\W` :利用basename取得工作目录名称，所以只会列出最后一个目录
　　`\#` :下达的第几个命令
　　`\$` :提示字符，如果是root时，提示符为：# ，普通用户则为：$

## 终端背景
终端背景一般默认纯色，且大多为黑色和白色。可以再终端的“设置”中开启背景透明，并选择合适的透明度，再挑选一张简约的深色图片做桌面背景。

通过以上的设置，是不是发现终端好看了很多，如果你有得意的美化方案配置，请致信`wangsheng.cas@gmail.com`讨论交流。

## 参考
linux PS1 提示符定义
[http://www.cnblogs.com/starspace/archive/2009/02/21/1395382.html](http://www.cnblogs.com/starspace/archive/2009/02/21/1395382.html)
dircolors-solarized项目主页
[https://github.com/seebi/dircolors-solarized](https://github.com/seebi/dircolors-solarized)
