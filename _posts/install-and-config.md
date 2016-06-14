---
title: 使用github和hexo搭建静态博客
date: 2016-06-08 22:48:22
categories: Hexo
tags: [Hexo]
---

Hello World
<!-- more -->
## github注册及建立仓储
1. 在[github主页](https://github.com)完成注册;
2. 验证邮箱;
3. 创建仓储，其中repository name必须为username.github.io;

## git的安装及添加ssh-key
在ubuntu下，使用以下命令安装git:
``` bash
$ sudo apt-get install git
$ git config --global user.email "Your emaill address"
$ git config --global user.name  "Your username on github.com"
```
使用以下命令生产ssh-key
``` bash
$ ssh-keygen -t rsa -C "Your email address"　#需要指定key文件名，使用默认即可
```
默认生成的ssh-key文件位于`~/.ssh/`目录下，其中的`id_rsa`和`id_rsa.pub`为我们需要的文件。将`id_rsa.pub`文件的文本内容添加到github的ssh-key中。使用以下命令测试是否成功:
``` bash
$ ssh -T git@github.com
```

## [hexo](https://hexo.io/)的安装

1.安装nvm
``` bash
$ wget -qO- https://raw.github.com/creationix/nvm/master/install.sh | sh
```
2.安装node.js
``` bash
$ nvm install v3.3
$ nvm ls #List installed versions
$ nvm use 3.3
$ nvm current #Display currently activated version
```
3.安装hexo
``` bash
$ npm install -g hexo
```

## 本地hexo初始化
1.初始化hexo目录
``` bash
$ hexo init ~/myblog
$ npm install
```
2.生成静态文件
``` bash
$ hexo g
```
3.本地服务器预览
``` bash
$ hexo s #打开浏览器通过http://0.0.0.0:4000/访问查看
```

## 发布
1.安装hexo-deployer-git
``` bash
$ npm install hexo-cli -g
```
<!-- $ npm install hexo-deployer-git --save --> <!-- old version --> 

2.在博客目录下找到`_config.yml`文件，添加或修改:
``` bash
deploy: 
	type: git
	repo: git@github.com:USERNAME/USERNAME.github.io.git
	branch: master
	message: "g"
```
注意，所有的冒号后面必须有空格！！！
3.发布
``` bash
$ hexo g
$ hexo d
```

## 预览
在浏览器中打开`http://USERNAME.github.io.git`页面访问静态博客。

## 添加博客文章并发布
使用以下命令添加新的文章至目录`\source\_posts\`:
``` bash
$ hexo new "article1"
```
随后可以在目录`\source\_posts\`中找到markdown格式文件`article1.md`。可以书写并修改其内容，然后使用以下命令发布:
``` bash
$ hexo clean
$ hexo g
$ hexo d
```

## 使用数学公式
安装[hexo-math](https://github.com/akfish/hexo-math)，随后即可在文章中插入公式。
``` bash
npm install hexo-math --save
```
可以在[hexo-math](https://github.com/akfish/hexo-math)项目主页找到如何插入公式。
配置过程中遇到的问题：[How to config it to make it work? #26](https://github.com/akfish/hexo-math/issues/26)
注意，[hexo-math](https://github.com/akfish/hexo-math)保持更新，且不同版本的安装与配置存在区别，在Google上搜索到的结果可能已经弃用了，所以以项目主页说明为准。


## 参考
github注册与入门
[`http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000`](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
搭建静态博客
[`http://blog.wpeace.cn/2015/07/22/%E4%BD%BF%E7%94%A8github%E5%92%8Chexo%E6%90%AD%E5%BB%BA%E9%9D%99%E6%80%81%E5%8D%9A%E5%AE%A2/`](http://blog.wpeace.cn/2015/07/22/%E4%BD%BF%E7%94%A8github%E5%92%8Chexo%E6%90%AD%E5%BB%BA%E9%9D%99%E6%80%81%E5%8D%9A%E5%AE%A2/)
ERROR Deployer not found: git
[`http://github.com/hexojs/hexo/issues/1154`](http://github.com/hexojs/hexo/issues/1154)

