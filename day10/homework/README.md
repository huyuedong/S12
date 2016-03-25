#这是一个通过RabbitMQ 实现远程命令分发和执行的程序

###作者介绍：
* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://blog.liwenzhou.com](http://blog.liwenzhou.com "liwenzhou's blog")

###功能介绍：
* 用RabbitMQ传递命令
* 用RPC远程执行命令，并返回结果

###环境依赖：
* Python3.0+

###目录结构：

    RabbitMQ_RPC_master
    ├── __init__.py
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── index.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    │   └── setting.py #全局变量配置文件
    ├── core #程序核心目录
    │   ├── __init__.py
    │   ├── rabbitmq_rpc_master.py #主核心
    │   └── Mylogging.py #log配置程序
    └── log #程序日志目录
        ├── __init__.py
        └── master.log #程序日志

    RabbitMQ_RPC_minion
    ├── __init__.py
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── index.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    │   └── minion.cfg #配置文件
    ├── core #程序核心目录
    │   ├── __init__.py
    │   ├── rabbitmq_rpc_minion.py #主核心
    │   └── Mylogging.py #log配置程序
    └── log #程序日志目录
        ├── __init__.py
        └── minion.log #程序日志


###运行说明：
* master端：运行RabbitMQ_RPC_master/bin/index.py即可。
* minion端：运行RabbitMQ_RPC_minion/bin/index.py即可。




