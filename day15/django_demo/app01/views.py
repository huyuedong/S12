from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse("This is the Home page!")


def index(request):
	return HttpResponse('This is app01.index')


# 登陆页面
def login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		# 如果登陆成功
		if username == "alex" and password == "1234":
			# 设置服务端session
			request.session["IS_LOGIN"] = True
			request.session["USERNAME"] = username
			return redirect("/order/")
	return render(request, "login.html")


# 订单页面
def order(request):
	is_login = request.session.get("IS_LOGIN", False)
	if is_login:
		username = request.session.get("USERNAME", False)
		# data = db[username]
		# return HttpResponse("order")
		return render(request, "order.html", {"username": username})
	else:
		return redirect("/login/")


def logout(request):
	del request.session["IS_LOGIN"]
	return redirect("/login/")
