# 这是一个利用paramiko实现的简易跳板机程序

### 作者介绍：
* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://blog.liwenzhou.com](http://blog.liwenzhou.com "liwenzhou's blog")

### 功能介绍：
* 所有的用户操作日志记录在数据库中
* 用户登录堡垒机，只需选择要连接的主机即可，无需再输入远程主机的用户名和密码。
* 用户对不同的目标设备有不同的访问权限。
* 对目标设备可以进行分组管理，允许用户访问某组设备，但是对组内的不同设备依然有不同的访问权限。

### 环境依赖：
* Python3.0+
* Paramiko
* Yaml
* MySQL

### 目录结构：

    StupidJumpServer
    ├── __init__.py
    ├── README.md
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── StupidJumpServer.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    │   ├── action_registers.py #菜单注册文件
    │   └── setting.py #全局变量配置文件
    ├── core #程序核心目录
    │   ├── __init__.py
    │   ├── actions.py #命令行启动入口
    │   ├── db_conn.py #数据库连接器
    │   ├── db_modles.py #数据库表结构模型
    │   ├── info_filter.py #数据过滤
    │   ├── interactive.py #交互核心
    │   ├── Mylogging.py #log配置文件
    │   ├── start_ssh.py #ssh连接核心
    │   ├── utils.py #yaml解析
    │   └── views.py #功能核心
    ├── home #yaml配置文件目录
    │   ├── __init__.py
    │   ├── new_users.yaml
    │   ├── new_groups.yaml
    │   ├── new_hostandsysuser.yaml
    │   └── new_hosts.yaml
    └── log #堡垒机程序日志目录
        ├── __init__.py
        └── StupidJumpServer.log #堡垒机程序日志



###运行说明：
* 建好数据库：StupidJumpServer
* 修改conf/setting.py中的数据库配置
* 运行bin/StupidJumpServer.py文件，根据提示完成初始化数据库、导入配置等操作。






