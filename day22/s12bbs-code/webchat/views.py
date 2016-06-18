from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse
from django.core.cache import cache
import os

# Create your views here.
from webchat import models
import queue,json,time

GLOBAL_MSG_QUEUES ={

}


@login_required
def dashboard(request):

    return render(request,'webchat/dashboard.html')


@login_required
def send_msg(request):
    print(request.POST)
    print(request.POST.get("msg"))
    #if request.POST.get()
    msg_data = request.POST.get('data')
    if msg_data:
        msg_data = json.loads(msg_data)
        msg_data['timestamp'] = time.time()
        if msg_data['type'] == 'single':
            if not GLOBAL_MSG_QUEUES.get(int(msg_data['to']) ):
                GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msg_data["to"])].put(msg_data)
    print(GLOBAL_MSG_QUEUES)
    #if not GLOBAL_MSG_QUEUES.get()
    return HttpResponse('---msg recevied---')

def get_new_msgs(request):


    if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
        print("no queue for user [%s]" %request.user.userprofile.id,request.user)
        GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()
    msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()
    q_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
    msg_list = []
    if msg_count >0:

        for msg in range(msg_count):
            msg_list.append(q_obj.get())

        print("new msgs:",msg_list)
    else:#没消息,要挂起
        print("no new msg for ",request.user,request.user.userprofile.id)
        #print(GLOBAL_MSG_QUEUES)

        try:
            msg_list.append(q_obj.get(timeout=60))
        except queue.Empty:
            print("\033[41;1mno msg for [%s][%s] ,timeout\033[0m" %(request.user.userprofile.id,request.user))
    return HttpResponse(json.dumps(msg_list))

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
