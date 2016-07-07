from django.shortcuts import render, HttpResponse
from django.utils.encoding import smart_str
from Stark import settings
import os
from django.http import FileResponse

# Create your views here.


def file_download(request):
	"""
	文件下载函数
	:param request:
	:return:
	"""
	file_path = request.GET.get("file_path")
	if file_path:
		file_center_dir = settings.SALT_CONFIG_FILES_DIR
		file_path = "{}{}".format(file_center_dir, file_path)
		print("file path:", file_path)
		file_name = file_path.split("/")[-1]

		response = FileResponse(open(file_path, "rb"))
		response['Content-Disposition'] = "attachment; filename={}".format(file_name)
		response["X-Sendfile"] = smart_str(file_path)

		return response
	else:
		raise KeyError
