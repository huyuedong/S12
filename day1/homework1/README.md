#这是一个登陆接口的Python小练习


* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://www.cnblogs.com/liwenzhou](http://www.cnblogs.com/liwenzhou "liwenzhou's blog")

###功能介绍：
输入用户名和密码
用户名不存在会提示
认证成功会显示欢迎信息
密码输入错误三次，当前用户名会被锁定

###环境依赖：
Python3.0+

###目录结构：
account.txt文件存储用户名和密码
lock.txt文件存储被锁定的用户名
login.py为主程序文件。实现完整程序功能依赖于account.txt、lock.txt文件。

###运行说明：
把account.txt、lock.txt、login.py这三个文件放在同一目录下，运行login.py即可。