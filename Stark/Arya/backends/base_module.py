#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


class BaseSaltModule(object):
    def __init__(self, sys_argvs, db_models):
        self.db_models = db_models
        self.sys_argvs = sys_argvs
        self.fetch_hosts()

    def fetch_hosts(self):
        print('--fetching hosts---')

        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h') + 1
                if len(self.sys_argvs) <= host_str_index:
                    exit("host argument must be provided after -h")
                else:  # get the host str
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list = self.db_models.Host.objects.filter(hostname__in=host_str_list)
                    print('----host list:', host_list)

        else:
            exit("host [-h] or group[-g] argument must be provided")