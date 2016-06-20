#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
上传文件处理
"""
import os


# 上传文件
def uploadfile_handle(request):
	f = request.FILES["head_img"]
	base_path = "uploads"
	user_path = "{}/{}".format(base_path, request.user.userprofile.id)
	if not os.path.exists(user_path):
		os.mkdir(user_path)
	file_path = "{}/{}".format(user_path, f.name)
	with open(file_path, "wb+") as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	return file_path
