#这是一个简单的批量主机管理工具

###作者介绍：
* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://blog.liwenzhou.com](http://blog.liwenzhou.com "liwenzhou's blog")

###功能介绍：
* 查看主机分组
* 增加主机分组、或者给主机分组添加主机
* 删除分组内的主机
* 对指定分组或多个分组的机器批量执行命令
* 对指定分组或多个分组的机器进行文件批量文件分发（发送/接收）

###环境依赖：
* Python3.0+

###目录结构：

    paramiko_homework
    ├── README
    ├── __init__.py
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── index.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    │   ├── config.json #主机分组配置文件
    │   ├── init_cfgfile.py #初始化配置文件
    │   └── setting.py #全局变量配置文件
    ├── core #程序核心目录
    │   ├── __init__.py
    │   ├── config_handler.py #主机分组配置文件处理程序
    │   ├── main.py #程序核心
    │   └── Mylogging.py #log配置程序
    ├── db #暂无内容
    └── log #程序日志目录
        ├── __init__.py
        └── all.log #程序目录

###运行说明：
* 在安装有Python3.0+版本的环境下,运行bin/index.py即可。

###补充说明：
* 两个测试账号：alex:1234, qimi:1234

