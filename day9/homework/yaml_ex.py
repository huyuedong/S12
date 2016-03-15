#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
Yaml练习
"""

import yaml

document = """
  a: 1
  b:
    c: 3
    d: 4
"""
print(yaml.dump(yaml.load(document)))

d1 = {
 "name": ["alex", "john", ],
 "age": [18, 20, ],
 "habit": "Girls",
}

print(yaml.dump(d1))

s1 = """
  - apple
  - starbucks
  - Nike
  - Hermes
"""

print(yaml.load(s1))

with open("sample.yml") as f:
    info = yaml.load(f)
    for i in info:
        print(i, info[i])
print(type(info))
