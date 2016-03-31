#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
管理员操作注册
用于定义管理员的操作类型
"""

import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import views

logger = logging.getLogger(__name__)


actions = {
	"start": views.start,
	# "stop": views.stop_server,
	"syncdb": views.syncdb,
	"create_users": views.create_users,
	"create_groups": views.create_groups,
	"create_hosts": views.create_hosts,
	"create_sysusers": views.create_sysusers,
	"create_create_hostandsysuser": views.create_hostandsysuser,
}
