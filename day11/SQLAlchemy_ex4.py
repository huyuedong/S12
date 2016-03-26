#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
外键关联
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:rootroot@localhost:3306/test", max_overflow=5)
Base = declarative_base()


class Host(Base):
	__tablename__ = "hosts"
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	ip_addr = Column(String(128), unique=True, nullable=False)
	port = Column(Integer, default=22)
	# group_id = Column(Integer, ForeignKey("group_id"))
	# group = relationship("Group")


class Group(Base):
	__tablename__ = "group"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# h1 = Host(hostname="localhost", ip_addr="127.0.0.1")
# h2 = Host(hostname="Ubuntu", ip_addr="192.168.0.1", port=10000)
# h3 = Host(hostname="CentOS", ip_addr="192.168.10.1")
#
# session.add_all([h1, h2, h3])

# g1 = Group(name="g1")
# g2 = Group(name="g2")
# g3 = Group(name="g3")
# g4 = Group(name="g4")
#
# session.add_all([g1, g2, g3, g4])





session.commit()
