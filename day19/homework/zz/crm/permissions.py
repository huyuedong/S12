#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
权限控制相关
"""

from django.shortcuts import render, HttpResponse, Http404, redirect
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User, Group


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
	print(request.user.get_group_permissions())  # 用户对应的组权限
	user = request.user
	user_groups = Group.objects.get(user=user)  # 获得用户的组
	print(user_groups)
	print("=" * 50)
	url_resolve_obj = resolve(request.path_info)  # 从请求中分解到到url对象
	current_url_namespace = url_resolve_obj.url_name  # 提取需要的url信息
	print(url_resolve_obj.kwargs)  # url参数
	url_kwargs = url_resolve_obj.kwargs

	if len(url_kwargs) > 0:
		if not url_kwargs.get("model_name_str", None) and url_kwargs.get("model_name_str") in role_groups.get(user_groups):
			print("{}没有权限操作表{}。".format(user, url_kwargs.get("model_name_str")))
			return False

	print("获取到url namespace:{}".format(current_url_namespace))
	match_flag = False  # 是否找到对应动作
	match_perm_key = None  # 动作对应的字段名
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
							match_flag = True  # 匹配上了
							match_perm_key = permission_key  # 获得该请求动作对应的权限字段名
							print("{} matched {}".format(request, permission_key))
							break  # 只要匹配到一个动作，就不再向下匹配动作
						else:  # 匹配动作参数
							request_method_func = getattr(request, request_method)  # request.GET或request.POST
							if all(map(request_method_func.get, request_args)):  # 如果请求中有动作规定的值
								match_flag = True  # 匹配上了
							else:
								match_flag = False
								break
	else:  # 没提取到url信息
		print(request.path_info)
		return True
	if match_flag:
		perm_str = "{}.{}".format(__package__, match_perm_key)
		if request.user.has_perm(perm_str):  # 用django自带的权限检测检测请求的用户是否有权限
			print("通过权限验证...")
			return True
		else:
			print("未通过权限验证...")
			print(request.user, perm_str)
			return False


def check_permission(func, redict_url="/crm/"):
	def wrapper(*args, **kwargs):
		print("开始进行权限认证！")
		if permission_check(*args, **kwargs) is not True:
			return render(args[0], "crm/403.html")
		return func(*args, **kwargs)
	return wrapper
