#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule
from Arya.backends import tasks
import os

class State(BaseSaltModule):

    def load_state_files(self,state_filename):
        from yaml import load, dump
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper
        state_file_path = "%s/%s" %(self.settings.SALT_CONFIG_FILES_DIR,state_filename)
        if os.path.isfile(state_file_path):
            with open(state_file_path) as f:
                data = load(f.read(), Loader=Loader)
                return data
        else:
            exit("%s is not a valid yaml config file" % state_filename)

    def apply(self):
        '''
        1. load the configurations file
        2. parse it
        3. create a task and sent it to the MQ
        4. collect the result with task-callback id
        :return:
        '''

        if '-f' in self.sys_argvs:
            yaml_file_index = self.sys_argvs.index('-f') + 1
            try:
                yaml_filename = self.sys_argvs[yaml_file_index]
                state_data = self.load_state_files(yaml_filename)
                #print('state data:',state_data)

                for os_type,os_type_data in self.config_data_dic.items(): #按照不同的操作系统单独生成一份配置文件
                    for section_name,section_data in state_data.items():
                        print('Section:',section_name)
                        for mod_name,mod_data in section_data.items():
                            base_mod_name = mod_name.split(".")[0]
                            module_obj=self.get_module_instance(base_mod_name=base_mod_name,os_type=os_type)
                            module_parse_result = module_obj.syntax_parser(section_name,mod_name,mod_data,os_type)
                            self.config_data_dic[os_type].append(module_parse_result)

                #代表上面的所有数据解析已完成 ，接下来生成一个任务，并把任务 放入队列
                print('config_data_dic'.center(60,'*'))
                print(self.config_data_dic)
                #生成新任务
                new_task_obj = tasks.TaskHandle(self.db_models,self.config_data_dic,self.settings,self)
                new_task_obj.dispatch_task()
            except IndexError as e:
                exit("state file must be provided after -f")

        else:
            exit("statefile must be specified.")
