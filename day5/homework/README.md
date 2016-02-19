#这是一个实现简单购物商城和ATM机的Python小程序

###作者介绍：
* author：liwenzhou
* nickname:Q1mi
* My Page:[liwenzhou.com](http://liwenzhou.com "liwenzhou's page")
* My Blog:[http://www.cnblogs.com/liwenzhou](http://www.cnblogs.com/liwenzhou "liwenzhou's blog")

###功能介绍：
* 基本实现了作业要求
* 购物商城登陆、注册，结算时调用信用卡接口。
* 信用卡支持额度查询、账单查询、修改密码、转账
* ATM支持多用户
* 信用卡支持取现，手续费5%
* 每个月22号出账单，每月10号为还款日，过期未还，按欠款总额的万分之五每日计息
* 记录账户每个月的消费流水
* 记录ATM机的操作日志
* ATM机管理员可以添加账户、调整额度、冻结账户、初始化密码

###环境依赖：
* Python3.0+

###目录结构：
atm_mall	
├── README
├── index.py #主程序入口
├── __init__.py
├── conf #配置文件
│   ├── __init__.py
│   ├── setting.py #参数
├── credit_card #ATM信用卡文件
│   ├── __init__.py
│   ├── admin_menu.py #管理员功能菜单
│   ├── card_main.py #ATM程序入口
│   ├── login.py #ATM登陆程序
│   ├── transaction_record.py #交易流水记录程序
│   └── user_menu.py #用户功能菜单
├── database #数据库文件
│   ├── __init__.py
│   ├── account.db #购物商城用户数据库
│   ├── card_account.db #信用卡用户数据库
│   ├── card_admin.db #ATM管理员数据库
│   ├── record.db #交易流水数据库
│   └── log.atm #ATM操作日志
├── general_module #通用模块文件
│   ├── __init__.py
│   ├── db_operater.py #数据库操作程序
│   ├── logger.py #日志记录程序
│   └── md5_encryption.py #密码加密程序
└── mall #购物商城文件
    ├── __init__.py
    ├── mall_login.py #购物商城登陆程序
    ├── mall_register.py #购物商城注册程序
    └── shopping_mall.py #购物商城程序入口

###运行说明：
* 在安装有Python3.0+版本的环境下,直接运行index.py文件即可。

###补充说明：
* 计息部分实现不够完整
