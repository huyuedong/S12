#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf.setting import DATABASE

engine_info = "{}+{}://{}:{}@{}:{}/StupidJumpServer".format(DATABASE.get("db_name"),
                                                            DATABASE.get("engine"),
                                                            DATABASE.get("username"),
                                                            DATABASE.get("password"),
                                                            DATABASE.get("host"),
                                                            DATABASE.get("port")
                                                            )

print(engine_info)
