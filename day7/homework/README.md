#这是一个实现简单FTP功能的Python小程序

###作者介绍：
* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://www.cnblogs.com/liwenzhou](http://www.cnblogs.com/liwenzhou "liwenzhou's blog")

###功能介绍：
* 基本实现了作业要求
* 允许同时多用户登录
* 每个用户有自己的家目录，且只能访问自己的家目录
* 对用户进行磁盘配额，每个用户的可用空间不同
* 允许用户在ftp server上随意切换目录
* 允许用户查看当前目录下的文件
* 允许上传和下载文件，保证文件一致性
* 文件传输过程中显示进度条


###环境依赖：
* Python3.0+
* Linux环境下使用

###目录结构：

    homework
    ├── README
    ├── __init__.py
    ├── ftpserver #ftp server程序
    │   ├── conf #配置文件
    │   │   ├── __init__.py
    │   │   └── setting.py #参数
    │   ├── bin #启动程序
    │   │   ├── __init__.py
    │   │   └── index.py #ftpserver执行文件
    │   ├── db #数据库文件
    │   │   ├── __init__.py
    │   │   ├── accounts.db #ftp用户数据库
    │   │   └── init_db.py #初始化用户数据库
    │   ├── home #家目录
    │   │   ├── alex #用户alex的家目录
    │   │   │   ├── test #用于测试的子目录
    │   │   │   └── test.jpg #用于下载测试的图片文件
    │   │   └── qimi #用户qimi的家目录
    │   ├── core #核心程序
    │   │   ├── __init__.py
    │   │   ├── db_handler.py #数据库操作引擎
    │   │   ├── ftp_log.py #日志函数
    │   │   └── ftp_server.py #ftp server主程序
    │   └── log #存放日志文件，暂未实现
    └── ftpclient #ftp client程序
        ├── __init__.py
        ├── home #存储用户上传文件的目录
        │    └── test.m4r #用于测试上传功能的音频文件
        └── ftp_client.py #ftp client执行文件

###运行说明：
* 在安装有Python3.0+版本的Linux环境下:
* * 运行bin下的index.py文件即可。

###补充说明：
* 暂不支持断点续传
