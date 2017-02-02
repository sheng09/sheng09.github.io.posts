---
title: 接收函数理论与实践（二）界面梯度对接收函数的影响
categories:
  - Receiver Function
tags:
  - Receiver Function
  - Interface
date: 2016-06-15 18:29:14
---

接收函数通过反褶积计算，提取波场在界面处的转换效应。在实际问题中，并不存在绝对的界面，更为准确的描述应该是速度梯度较高的过度带。为对比梯度带给接收函数波形带来的影响，参考[CPS Tutorials部分内容](http://www.eas.slu.edu/eqc/eqc_cps/TUTORIAL/RFTN2/index.html)，本文选择了走时相同，梯度变化不同的模型，用于接收函数正演计算。
<!-- more -->
<!-- toc -->
## 模型设定
生成不同的梯度界面模型，并合理配置使走时相同。模型S波速度，P波速度及密度如下图所示，不同颜色的实线代表不同的模型。

<table>
<tr>
  <td> <img src="/RF-interface-02/VS.jpg"  width=250 align=center /> </td>
  <td> <img src="/RF-interface-02/VP.jpg"  width=250 align=center /> </td>
  <td> <img src="/RF-interface-02/RHO.jpg" width=250 align=center /> </td>
</tr>
</table>

## 正演结果
<img src="/RF-interface-02/rf_prf.jpg"      width=500 align=center/>
<img src="/RF-interface-02/rf_rainbow.jpg"  width=500 align=center/>

## 运行
下载[rf_interface](/exam/rf_interface.tgz)，解压，运行如下：
``` bash
$ cd
$ ./run.sh          #生成模型并正演
$ ./PlotModels.sh   #绘制模型图
```
文件结构如下：
``` tree
rf_interface/
├── PlotModels.sh    #scripts
├── run.sh
├── rf_prf.jpg       #generated diagrams
├── rf_rainbow.jpg
├── rf_sac.jpg
├── RayPath.c        #program for calculating raypath for specific seismic phase
├── mkgrad.f         #program for generate models, from ‘CPs’
├── CalRayPara.py    #python scripts for calculating ray parameters
├── CalTrvTPPPS.py   #python scripts for calculating traveltimes
├── CalTrvTPPSS.py
├── CalTrvTPS.py
├── CalTrvTPSSS.py
├── Grad_Intf_RFS/   #generate RF waveform for models
│   ├── RF.0.0618.00.sac
│   ├── ...
└── models/          #models and diagrams
    ├── Grad_Intf_hrftn96_00.model #model
    ├── Grad_Intf_hrftn96_00.ps    #single model plot and raypath
    ├── ...
    ├── RHO.jpg      #models set plot
    ├── VP.jpg
    └── VS.jpg
```
如果对程序有任何疑问，或者发现任何BUG，请留言，或者致信`wangsheng.cas@gmail.com`。
