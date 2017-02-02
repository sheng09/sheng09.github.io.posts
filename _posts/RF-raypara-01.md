---
title: 接收函数理论与实践（一）射线参数对接收函数的影响
categories:
  - Receiver Function
tags:
  - Receiver Function
  - 射线参数
date: 2016-06-15 17:40:28
---

本文正演计算了不同射线参数（震中距）对应的接收函数波形，以对比震相随射线参数的变化。正演计算和图形绘制的程序可以点击下载[rf_raypara](/exam/rf_raypara.tgz)。程序使用需要预装[CPS](http://www.eas.slu.edu/eqc/eqccps.html)和[GMT_v4](http://gmt.soest.hawaii.edu/)软件包。
<!-- more -->
<!-- toc -->
## 模型设定
构建一维地壳模型`./model.dat`。模型如下图所示。分别绘制了Pp，Ps，PpPs，PpSs+PsPs震相的射线路径图，其中，蓝色实线代表P波路径，红色实线代表S波路径。
<img src="/RF-raypara-01/model.jpg" width=500 align=center />

绘图命令如下：
``` bash
$ cd rf_raypara/
$ ./PlotModel.sh
```

## 正演
选取不同的射线参数，范围为[0.14, 1.0e-5) s/km，选取高斯参数为1.0，做正演计算。其中，射线参数越小，代表震中距越大，射线越接近垂直入射。运行如下：
``` bash
$ cd rf_raypara/
$ ./run.sh
```
实际数据提取接收函数，一般选取震中距位于30°～90°范围内的地震事件记录，在iasp91模型中，对应的射线参数位于[0.04, 0.08]范围内。
<img src="/RF-raypara-01/rp_prf.jpg" width=600 align=center />

由正演结果，可以发现30°～90°震中距范围内，Ps震相随射线参数变化不大，而PpPs，PpSs+PsPs震相则呈现较为明显的变化。
针对转换波震相到时随射线参数的变化，接收函数叠加需要做动校正，或者按射线参数分区间叠加。

## 注意事项
[rf_raypara](/exam/rf_raypara.tgz)包含了本文需要的所有程序，其中`Raypath`由`Raypath.c`编译而来，编译命令如下：
``` bash
$ cd rf_raypara/
$ gcc Raypath.c -o Raypath -lm -O4
```
[rf_raypara](/exam/rf_raypara.tgz)的`.sh`,`.py`脚本需要添加可执行权限，命令如下:
``` bash
$ cd rf_raypara/
$ chmod +x *.py *.sh
```
如果对程序有任何疑问，或者发现任何BUG，请留言，或者致信`wangsheng.cas@gmail.com`。
