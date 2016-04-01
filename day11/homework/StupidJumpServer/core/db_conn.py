#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
数据库连接对象
"""
import os
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf.setting import DATABASE

logger = logging.getLogger(__name__)

engine_info = "{}+{}://{}:{}@{}:{}/{}".format(
		DATABASE.get("db_type"),
		DATABASE.get("engine"),
		DATABASE.get("username"),
		DATABASE.get("password"),
		DATABASE.get("host"),
		DATABASE.get("port"),
		DATABASE.get("db_name"),
)

engine = create_engine(engine_info, echo=False)
SessionCls = sessionmaker(bind=engine)
session = SessionCls()
