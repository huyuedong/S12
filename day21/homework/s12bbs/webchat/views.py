from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from webchat import models as webchat_models
from bbs import models as bbs_models
import queue
import json
import time
import os

# Create your views here.

# 从数据库中找出所有set_as_top_menu=True的版块，并按照position_index排序
category_list = bbs_models.Category.objects.filter(set_as_top_menu=True).order_by("position_index")

GLOBAL_MSG_QUEUES = {

}


# 状态装饰器,只要用户开始收消息就写一个五分钟的cache
def set_status(func):
	def inner(arg):
		print("start decorator:set_status...")
		status_key = "{}_status".format(arg.user.userprofile.id)
		print("status key==>", status_key)
		cache.set(status_key, 1, 300)  # 保存用户在线状态5分钟
		return func(arg)  # 继续执行取消息的方法
	return inner


@login_required(login_url="/login/")
@set_status
def dashboard(request):
	print(request.user.userprofile.group_members.select_related())
	return render(request, "webchat/dashboard.html", {'category_list': category_list})


@login_required(login_url="/login/")
@set_status
def send_msg(request):
	print("get data from send_msg...")
	print(request.POST)
	msg_data = request.POST.get("data")
	print(msg_data)
	if msg_data:
		msg_data = json.loads(msg_data)
		if msg_data.get("to"):  # 确保接收到的消息有to属性
			msg_to_obj = bbs_models.UserProfile.objects.get(id=msg_data["from"])  # 发送消息的人
			msg_data["nickname"] = msg_to_obj.name  # 发消息的人的名字
			msg_data["hd_img"] = msg_to_obj.get_head_img()  # 头像
			msg_data["timestamp"] = time.strftime("%H:%M:%S", time.localtime(time.time()))  # 消息的时间戳
			print(msg_data)
			global msg_to_list  # 消息接收人列表
			if msg_data["type"] == "single":  # 发送给单人
				msg_to_list = [int(msg_data["to"]), ]  # msg_data中的值都是字符串类型
			elif msg_data["type"] == "group":  # 群发消息
				msg_data["from"] = msg_data["to"]  # 群发消息的发送者默认为群组的id,发消息认得信息在上面已经提取出来了
				webgroup_obj = webchat_models.WebGroup.objects.get(id=msg_data["to"])  # 找到群对象
				members_obj_set = webgroup_obj.members.select_related()
				msg_to_list = [member.id for member in members_obj_set]
				msg_to_list.remove(request.user.userprofile.id)  # 收消息的人中移除自己
			print(msg_to_list)
			for to_id in msg_to_list:  # 遍历将消息放进queue
				if not GLOBAL_MSG_QUEUES.get(int(to_id)):  # 没有该对象的queue就新建，注意id值是否需要转换
					GLOBAL_MSG_QUEUES[int(to_id)] = queue.Queue()
				GLOBAL_MSG_QUEUES[int(to_id)].put(msg_data)  # 把消息数据放入queue
	else:
		print("invalid request post data:{}".format(request.POST))
	return HttpResponse("msg received.")


@login_required(login_url="/login/")
@set_status
def get_new_msgs(request):
	if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
		GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()  # 这里的id值是int类型
	msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()  # 获取未读消息数
	queue_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
	msg_list = []
	if msg_count > 0:
		for i in range(msg_count):
			msg_list.append(queue_obj.get())
	else:  # 没有消息，挂起
		print("no msg for {}(id:{})".format(request.user.userprofile.name, request.user.userprofile.id))
		try:
			msg_list.append(queue_obj.get(timeout=60))  # 60秒超时
		except queue.Empty:
			print("\033[41;1mNo msg for {}(id:{}),timeout.\033[0m".format(
					request.user.userprofile.name,
					request.user.userprofile.id
			))
	return HttpResponse(json.dumps(msg_list))


@login_required(login_url="/login/")
def check_my_friends_status(request):
	print("get request from frontend to get online friends...")
	my_friends_list = request.user.userprofile.friends.select_related()
	online_friends_list = []
	for my_friend_obj in my_friends_list:
		if cache.get("{}_status".format(my_friend_obj.id)):
			online_friends_list.append(my_friend_obj.id)
	print("online list==>", online_friends_list)
	return HttpResponse(json.dumps(online_friends_list))


@login_required(login_url="/login/")
def upload_file(request):
	if request.method == "POST":
		print("in post...")
		f = request.FILES["file"]
		print(f)
		base_path = "uploads"
		user_path = "{}/{}".format(base_path, request.user.userprofile.id)
		if not os.path.exists(user_path):
			os.mkdir(user_path)
		file_path = "{}/{}".format(user_path, f.name)
		recv_size = 0
		with open(file_path, "wb+") as destination:
			for chunk in f.chunks():
				destination.write(chunk)
				recv_size += len(chunk)  # 累加已传文件大小
				cache.set(f.name, recv_size)  # 设置文件名及已传大小
		return HttpResponse(file_path)
	else:
		return render(request, "webchat/test.html")


def upload_file_progress(request):
	filename = request.GET.get("filename")
	progress = cache.get(filename)
	print("file:{}, uploading progress:{}.".format(filename, progress))
	return HttpResponse(json.dumps({"recv_size": progress}))


def delete_cache_key(request):
	cache_key = request.GET.get("cache_key")
	cache.delete(cache_key)
	return HttpResponse("cache key :{} has deleted...".format(cache_key))
