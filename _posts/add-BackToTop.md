---
title: Hexo博客添加返回顶部按钮
date: 2016-06-14 15:49:54
categories: [Hexo] 
tags: [Hexo]
---

为博客添加一个`返回顶部`的按钮，简单而又实用。
<!-- more -->
<!-- toc -->
## 添加HTML代码
为网页添加`返回顶部`的代码，在主题目录下新建`source/_partial/totop.ejs`，写入内容
``` html
<div id="totop" style="position:fixed;bottom:150px;right:20px;cursor: pointer;">
	<a title="Back to top"><img src="/imgs/scrollup_arrow.png"/></a>
</div>
```
其中，选择自己满意的图片`src="/imgs/scrollup_arrow.png"`设置按钮，以及与网页相衬的`style`。

## 添加JS代码
为我们的`返回顶部`按钮添加JS代码。在主题目录下新建文件`source/js/totop.js`，写入内容
``` javascript
(function($) {
	// When to show the scroll link
	// higher number = scroll link appears further down the page
	var upperLimit = 1000;
	// Our scroll link element
	var scrollElem = $('#totop');
	// Scroll to top speed
	var scrollSpeed = 500;
	// Show and hide the scroll to top link based on scroll position
	scrollElem.hide();
	$(window).scroll(function () {
		var scrollTop = $(document).scrollTop();
		if ( scrollTop > upperLimit ) {
			$(scrollElem).stop().fadeTo(300, 1); // fade back in
		}else{
			$(scrollElem).stop().fadeTo(300, 0); // fade out
		}
	});

	// Scroll to top animation on click
	$(scrollElem).click(function(){
		$('html, body').animate({scrollTop:0}, scrollSpeed); return false;
	});
})(jQuery);
```

## 添加对以上代码的引用
打开主题目录下的文件`/layout/_partial/after_footer.ejs`，在文件末尾添加以下内容
``` html
<%- partial('totop') %>
<script src="<%- config.root %>js/totop.js"></script>
```
完成！
