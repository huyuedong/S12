#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import ftp_server


if __name__ == "__main__":
	ftp_server.run()
