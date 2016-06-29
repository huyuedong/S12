#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


class BaseSaltModule(object):
    def __init__(self, sys_argvs, db_models, settings):
        self.db_models = db_models
        self.settings = settings
        self.sys_argvs = sys_argvs
        self.host_list = []

    def get_os_types(self):
        data = {}
        for host in self.host_list:
            data[host.os_type] = []
        return data

    def process(self):
        """
        处理参数，将主机按OS类型分组
        :return:
        """
        self.fetch_hosts()
        self.config_data_dic = self.get_os_types()

    def require(self):
        """
        处理需要解决的依赖
        :return:
        """
        pass

    def fetch_hosts(self):
        print('--fetching hosts---')

        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h') + 1
                if len(self.sys_argvs) <= host_str_index:
                    exit("host argument must be provided after -h")
                else:  # get the host str
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list.extend(self.db_models.Host.objects.filter(hostname__in=host_str_list))
                    print('----host list:', host_list)
            if "-g" in self.sys_argvs:
                group_str_index = self.sys_argvs.index["-g"] + 1
                if len(self.sys_argvs) <= group_str_index:
                    exit("group argument must be provided after -g")
                else:
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(",")
                    group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list)
                    for group in group_list:
                        host_list.extend(group.hosts.selected_related())
            self.host_list = list(set(host_list))
            print("get host list:", self.host_list)
            return True

        else:
            exit("host [-h] or group[-g] argument must be provided")

    def syntax_parser(self, section_name, module_name, module_data):
        print("going to parser state data:", section_name, module_name)
        for state_item in module_data:
            print("\t", state_item)
            for key in state_item:
                if hasattr(self, key):
                    state_func = getattr(self, key)
                    state_func(state_item[key])
                else:
                    exit("Error:module:{} has no argument:{}.".format(module_name, key))
