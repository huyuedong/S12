#! /usr/bin/env python
# -*- coding: utf-8 -*-

loop1 = 0
loop2 = 0
while True:
    loop1 += 1
    print("父循环：", loop1)
    break_flag = False
    while True:
        loop2 += 1
        if loop2 == 5:
            break_flag = True
            print("跳出子循环！")
            break
        print("子循环：", loop2)
    if break_flag:
        print("跳出父循环！")
        break
