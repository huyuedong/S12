#这是一个实现简单小游戏的Python小程序

###作者介绍：
* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://www.cnblogs.com/liwenzhou](http://www.cnblogs.com/liwenzhou "liwenzhou's blog")

###功能介绍：
* 基本实现了作业要求
* 至少有两个不同的角色
* 玩的过程中，必须要有冲突。（角色之间要有交互）。
* 根据不同的交互，产生不同的行为。
* 让用户可以玩。
* 一定要用到面向对象编程的语法与思想。

###环境依赖：
* Python3.0+

###目录结构：

    the_life
    ├── README
    ├── __init__.py
    ├── conf #配置文件
    │   ├── __init__.py
    │   ├── setting.py #参数
    ├── bin #启动程序
    │   ├── __init__.py
    │   └── the_life.py #游戏执行文件
    ├── db #数据库文件
    │   ├── __init__.py
    │   ├── 20160225_132926 #存档文件
    │   ├── 20160225_134849 #存档文件
    │   ├── 20160225_142042 #存档文件
    │   ├── 20160225_142606 #存档文件
    │   └── 20160225_142700 #存档文件
    └── core #核心程序
        ├── __init__.py
        ├── db_handler.py #数据库连接模块
        ├── main.py #游戏主逻辑模块
        ├── role_module.py #游戏角色定义模块
        └── save_data.py #游戏存档模块

###运行说明：
* 在安装有Python3.0+版本的环境下,直接运行bin下的the_life.py文件即可。

###补充说明：
* 游戏多角色之间的交互实现不够完整
