# SeleniumFrameWork
## 简介
这是一个selenium的自动化测试框架，主要是将一些自动化测试的概念融合在一起：
* 使用unittest框架来组织测试的执行
* 参考了`https://www.cnblogs.com/yufeihlf/p/5764099.html`的Page Object模式，将控件定位和操作分开，后续页面如果变更了，无需更改操作代码，低耦合
* 使用了DDT框架来做数据驱动测试
* 使用了logging模块做日志的记录
* 使用了HtmlTestRunner来生成html报告

## 目录结构
* Data文件夹：存档测试数据
* Images文件夹：存放截图文件
* Logs文件夹：存放日志
* Pages文件夹：存放各页面的控件定位器和操作代码，以页面为单位
* Report文件夹：存放测试报告
* Utils文件夹：工具类文件夹，存放常用工具
* PageTest.py：unittest测试框架
