from django.shortcuts import render, HttpResponse
from testapp.forms import select_test

# Create your views here.


def test(request):
	f = select_test.SelectTestForm(initial={"city": 2, "modes": [2, ]})  # 方法2
	if request.method == "POST":
		print(request.POST)
		return HttpResponse("OK")
	else:
		return render(request, "test/select_test.html", {"f": f})
