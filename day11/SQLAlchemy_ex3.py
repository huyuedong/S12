#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
使用 ORM/Schema Type/SQL Expression Language/Engine/ConnectionPooling/Dialect 所有组件对数据进行操作。根据类创建对象，对象转换成SQL，执行SQL。
增删改查
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:rootroot@localhost:3306/test", max_overflow=5)
Base = declarative_base()


class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	name = Column(String(50))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ================增=====================
u = User(id=2, name="John")
session.add(u)
session.add_all([
	User(id=3, name="Tom"),
	User(id=4, name="Mask")
])
session.commit()

# ===============删除====================
session.query(User).filter(User.id > 2).delete()
session.commit()

# ===============修改====================
session.query(User).filter(User.id > 2).update({"cluster":0})
session.commit()

# ===============查======================
ret = session.query(User).filter_by(name="John").first()
ret = session.query(User).filter_by(name="John").all()
print(ret)

ret = session.query(User).filter(User.name.in_(["Tom", "Mask"])).all()
print(ret)

ret = session.query(User.name.label("name_label")).all()
print(ret, type(ret))

ret = session.query(User).order_by(User.id).all()
print(ret)

ret = session.query(User).order_by(User.id)[1:3]
print(ret)
session.commit()
