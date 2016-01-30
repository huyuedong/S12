#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
import sys
import os
from backend.logic import handle

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)


handle.home()
