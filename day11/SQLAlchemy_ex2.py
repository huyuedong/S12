#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
SQLAlchemy高级练习
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


Base = declarative_base()  # 生成一个SqlORM基类

# echo不回显
engine = create_engine("mysql+pymysql://root:rootroot@localhost:3306/test", echo=False)


class Host(Base):
	__tablename__ = "hosts"
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	ip_addr = Column(String(128), unique=True, nullable=False)
	port = Column(Integer, default=22)

Base.metadata.create_all(engine)

if __name__ == "__main__":
	SessionCls = sessionmaker(bind=engine)
	session = SessionCls()
	h1 = Host(hostname="localhost", ip_addr="127.0.0.1")
	h2 = Host(hostname="ubuntu", ip_addr="192.168.0.1")
	h3 = Host(hostname="CentOS", ip_addr="192.168.1.1")
	session.add(h3)
	session.add_all([h1, h2])
	# h2.hostname = "ubuntu_test"  # 只要没提交，此时修改也可以
	# session.rollback()
	session.commit()
	# res = session.query(Host).filter(Host.hostname.in_(["CentOS", "localhost"])).all
	# print(res)
