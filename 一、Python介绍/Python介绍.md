# Python 介绍

## 一、简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

+ **Python 是一种解释型语言:** 这意味着开发过程中没有了编译这个环节。类似于 `PHP` 和 `Perl`语言。
+ **Python 是交互式语言：** 这意味着，您可以在一个 `Python` 提示符 `>>>` 后直接执行代码。
+ **Python 是面向对象语言:** 这意味着 `Python` 支持面向对象的风格或代码封装在对象的编程技术。
+ **Python 是初学者的语言：** `Python` 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

什么是解释型语言

> 每次执行程序都需要一边转换一边执行，用到哪些源代码就将哪些源代码转换成机器码，用不到的不进行任何处理。每次执行程序时可能使用不同的功能，这个时候需要转换的源代码也不一样。
>>解释型语言和编译型语言
>>| 类型 |原理|优点|缺点|
>>|:--:|---|---|---|
>>|编译型语言|通过专门的编译器，将所有源代码一次性转换成特定平台（`Windows、Linux` 等）执行的机器码（以可执行文件的形式存在）。|编译一次后，脱离了编译器也可以运行，并且运行效率高。|可移植性差，不够灵活。|
>>|解释型语言|由专门的解释器，根据需要将部分源代码临时转换成特定平台的机器码。|跨平台性好，通过不同的解释器，将相同的源代码解释成不同平台下的机器码。|一边执行一边转换，效率低。|

## 二、特点

1. 语法简单、易于学习
2. 易于阅读、维护
3. 可移植、可扩展、可嵌入


## 三、环境搭建

`Python` 可以运行在 `Wiindows、Linux、MacOS` 等多个平台。

### 下载

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 安装

`Windows` 系统下，傻瓜式安装，直接按照安装界面，一直点击下一步即可。安装完后，设置环境变量,在命令行(cmd)中输入：

```cmd
path=%path%;python的安装目录
```

安装完之后，打开命令行(cmd),直接输入 `Python` ,如果出现类似如下内容，说明安装成功：

```cmd
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

### 开发工具

1. 官方自带工具
2. `Visual Studio Code`，需要安装 `Python` 相关插件支持。例如：
   + [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   + [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
3. 其他工具
