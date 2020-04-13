# flask-cy
Flask写的在线词云生成工具

[![GitHub stars](https://img.shields.io/github/stars/cjh0613/flask-cy.svg?style=social)](https://github.com/cjh0613/flask-cy/stargazers)     [![GitHub forks](https://img.shields.io/github/forks/cjh0613/flask-cy.svg?style=social)](https://github.com/cjh0613/flask-cy/network/members)  `请点击页面顶部靠右star与fork`


[![GitHub release](https://img.shields.io/github/release/cjh0613/flask-cy.svg?label=%E7%89%88%E6%9C%AC)](https://github.com/cjh0613/flask-cy/releases/tag/)   ![GitHub top language](https://img.shields.io/github/languages/top/cjh0613/flask-cy.svg)  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjh0613/flask-cy.svg)  ![GitHub repo size](https://img.shields.io/github/repo-size/cjh0613/flask-cy.svg) ![GitHub](https://img.shields.io/github/license/cjh0613/flask-cy.svg) ![platforms](https://img.shields.io/badge/platform-win32%20%7C%20win64%20%7C%20linux%20%7C%20osx-brightgreen.svg)     [![GitHub issues](https://img.shields.io/github/issues/cjh0613/flask-cy.svg)](https://github.com/cjh0613/flask-cy/issues)  [![GitHub closed issues](https://img.shields.io/github/issues-closed/cjh0613/flask-cy.svg)](https://github.com/cjh0613/flask-cy/issues?q=is%3Aissue+is%3Aclosed) ![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjh0613/flask-cy.svg)   ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/cjh0613/flask-cy.svg)  ![GitHub contributors](https://img.shields.io/github/contributors/cjh0613/flask-cy.svg)


请使用windows+python3环境

推荐使用wheel方式安装所需要的wordcloud等模块

pip install matplotlib

worldcloud无法用pip安装，下载地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud


![112.png](https://i.loli.net/2019/07/18/5d2fda1fab42189708.png)]
### 简介
#### 写着玩的，代码比较粗糙，技术含量也比较低！

这是一个分析词频的网站，可以将分析结果生成一张图片。你可以将一篇文章，
一些采集结果或者其他文本数据粘贴其中，点击“分析一下”，即可展示结果。
图片中的关键词字体越大，代表关键词出现的频率越高，反之亦然。

### 各个文件夹说明
fonts 存放字体文件

images 存放生成的图片（同时也会上传到sm.ms）

templates 存放模板文件

text 存放用户分析的文本


传送门：http://localhost/cytools/


### 相关截图：
[![112.png](https://i.loli.net/2019/07/17/5d2ef71da938694339.png)](https://i.loli.net/2019/07/17/5d2ef71da938694339.png)


