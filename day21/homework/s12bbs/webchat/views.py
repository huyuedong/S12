from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from webchat import models
import queue
import json
import time

# Create your views here.

GLOBAL_MSG_QUEUES = {

}


@login_required
def dashboard(request):
	return render(request, "webchat/dashboard.html")


@login_required
def send_msg(request):
	msg_data = request.POST.get("msg")
	if msg_data:
		msg_data = json.loads(msg_data)
		msg_data["timestamp"] = time.time()
		if msg_data["type"] == "single":  # 发送给单人
			if not GLOBAL_MSG_QUEUES.get(int(msg_data["to"])):  # 没有该对象的queue就新建，这里的id值是字符串类型需要转换
				GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()
			GLOBAL_MSG_QUEUES[int(msg_data["to"])].put(msg_data)  # 把消息数据放入queue
	return HttpResponse("msg received.")


@login_required
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
			print("\033[41;1mNo msg for {}(id:{}),timeout.\033[0m".format(request.user.userprofile.name, request.user.userprofile.id))
	return HttpResponse(json.dumps(msg_list))
