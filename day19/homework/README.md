# 这是CRM的练习

#### 作者介绍：
* author：liwenzhou
* nickname: Q1mi
* My Page: [www.liwenzhou.com](http://www.liwenzhou.com "liwenzhou's page")
* My Blog: [http://blog.liwenzhou.com](http://blog.liwenzhou.com "liwenzhou's blog")

#### 功能介绍：
* 类似Django Admin的界面
* 实现展示、搜索、过滤等功能
* 自定义权限管理


#### 使用方法：
* 输入：http://127.0.0.1:8000/crm/进行操作
* 测试账户：2@2.com 1234567

#### 目录结构：
    homework
    ├── README.md
    └── zz #Django Project文件
        ├── cmdb #上次作业的app
        ├── static #静态文件
        ├── templates #模板文件
        ├── zz #默认app
        ├── db.sqlite3 #数据库文件
        ├── manage.py #
        └── crm #此次作业app,文件都在这里面
           ├── forms #form文件
           ├── migrations #
           ├── templatetags #自定义simpletag文件
           ├── __init__.py
           ├── admin.py #
           ├── apps.py #
           ├── models.py #数据库模型文件
           ├── permissions.py #权限验证文件
           ├── tests.py #
           ├── urls.py #url路由文件
           └── views.py #视图文件

#### 备注：
* 测试账号：
    * teachers group: alex alex1234
    * salesman group: zhangsan alex1234
    * students group: liwenzhou alex1234