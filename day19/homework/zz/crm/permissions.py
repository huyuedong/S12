#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
权限控制相关
"""

from django.shortcuts import render, HttpResponse, Http404, redirect
from django.core.urlresolvers import resolve


# 定义角色分组，不同的组只能对指定的model有相关权限
role_groups = {
	"salesman": ["Customer", "ConsultRecord"],
	"teachers": ["Course", "ClassList", "CourseRecord", "StudyRecord"],
	"students": ["StudyRecord"],
}

# 权限与动作对应关系
permission_dic = {
	"view_index": ["crm_index", "GET", []],  # 查看首页
	"view_record_details": ["model_detail", "GET", []],  # 查看记录详情
	"change_record_details": ["change_model_detail", "POST", []],  # 修改记录详情
	"add_record": ["add_model_detail", "POST", []],  # 增加记录
	"delete_record": ["delete_model", "POST", []]  # 删除记录
}


# 进项权限验证
def permission_check(*args, **kwargs):
	request = args[0]  # 默认第一个参数时request
	url_resolve_obj = resolve(request.path_info)  # 从请求中分解到到url对象
	current_url_namespace = url_resolve_obj.url_name  # 提取需要的url信息
	print("获取到url namespace:{}".format(current_url_namespace))
	match_flag = False  # 是否找到对应动作
	match_prem_key = None  # 动作对应的字段名
	if current_url_namespace:
		print("开始匹配动作...")
		for permission_key in permission_dic:
			permission_value = permission_dic[permission_key]
			if len(permission_value) == 3:  # 判断是不是有效的权限动作设置
				url_namespace, request_method, request_args = permission_value
				print(url_namespace, request_method, request_args)
				if url_namespace == current_url_namespace:  # url匹配
					if request_method == request.method:  # 请求的方法匹配
						if not request_args:  # 如果没有动作参数
							match_flag = True
							match_prem_key = permission_key
							print("{} matched {}".format(request, permission_key))
							break  # 只要匹配到一个动作，就不再向下匹配动作
						else:  # 匹配动作参数
							request_method_func = getattr(request, request_method)  # request.GET或request.POST
							if all(map(request_method_func, request_args)):
								pass


def check_permission(func, redict_url="/index/"):
	def wrapper(*args, **kwargs):
		print("开始进行权限认证！")
		if permission_check() is not True:
			return render(args[0], redict_url)
		return func(*args, **kwargs)
	return wrapper
