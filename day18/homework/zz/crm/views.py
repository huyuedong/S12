from django.shortcuts import render, HttpResponse
from cmdb.auth import auth

# Create your views here.


@auth.acc_auth
def index(request):
	user = request.session["NAME"]
	return render(request, "crm/index.html", {"username": user})

