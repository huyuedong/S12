from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from webchat import models as webchat_models
from bbs import models as bbs_models
import queue
import json
import time

# Create your views here.

# 从数据库中找出所有set_as_top_menu=True的版块，并按照position_index排序
category_list = bbs_models.Category.objects.filter(set_as_top_menu=True).order_by("position_index")

GLOBAL_MSG_QUEUES = {

}


@login_required(login_url="/login/")
def dashboard(request):
	return render(request, "webchat/dashboard.html", {'category_list': category_list})


@login_required(login_url="/login/")
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