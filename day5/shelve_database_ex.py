#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
一个shelve写的简易数据库
"""

# database.py
import sys, shelve


def store_person(db):
    """
    Query user for data and store it in the shelf object
    """
    pid = input('Enter unique ID number: ')
    goods = {}
    goods['name'] = input('Enter trade name: ')
    goods['info'] = input('Enter trade info: ')
    goods['price'] = input('Enter price: ')
    goods['stock'] = input('Enter stock number: ')
    db[pid] = goods


def lookup_person(db):
    """
    Query user for ID and desired field, and fetch the corresponding data from
    the shelf object
    """
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()
    print('{}:{}'.format(field.capitalize(), db[pid][field]))


def print_help():
    print('The available commons are: ')
    print('store  :Stores information about a person')
    print('lookup :Looks up a person from ID number')
    print('quit   :Save changes and exit')
    print('?      :Print this message')


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
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()
if __name__ == '__main__':
    main()
