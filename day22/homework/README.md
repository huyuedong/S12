# 这是网页聊天室的练习

#### 作者介绍：
* author：liwenzhou
* nickname: Q1mi
* My Page: [www.liwenzhou.com](http://www.liwenzhou.com "liwenzhou's page")
* My Blog: [http://blog.liwenzhou.com](http://blog.liwenzhou.com "liwenzhou's blog")

#### 功能介绍：
* 类似网页版微信的界面
* 实现单聊、群聊、发送图片、文件等功能
* 好友在线状态的显示
* 好友搜索
* 发送表情



#### 使用方法：
* 输入：http://127.0.0.1:8000/webchat/进行操作
* 测试账户：qimi qimi1234; alex alex1234

#### 目录结构：
    homework
    ├── README.md
    └── s12bbs #Django Project文件
        ├── bbs #上次作业的app
        ├── static #静态文件
        ├── templates #模板文件
        ├── s12bbs #默认app
        ├── db.sqlite3 #数据库文件
        ├── manage.py #
        ├── uploads #上传文件保存的目录    
        └── webchat #此次作业app,文件都在这里面
           ├── migrations #
           ├── __init__.py
           ├── admin.py #
           ├── apps.py #
           ├── models.py #数据库模型文件
           ├── tests.py #
           ├── urls.py #url路由文件
           └── views.py #视图文件

#### 备注：
* 测试账号：
    * qimi: qimi1234
    * alex: alex1234
    * rain: alex1234
    * james: alex1234
    * wade: alex1234
    * eric: alex1234