#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import shelve
from collections import OrderedDict


def store_person(db):
    """
    Query user for data and store it in the shelf object
    """
    pid = input('Enter unique ID number: ')
    goods = OrderedDict()
    goods['name'] = input('Enter trade name: ')
    goods['info'] = input('Enter trade info: ')
    goods['price'] = input('Enter price: ')
    goods['stock'] = input('Enter stock number: ')
    db[pid] = goods


def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('trade_db')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == "__main__":
    main()
