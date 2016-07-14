from django.shortcuts import render, HttpResponse

# Create your views here.


def test(request):
	if request.method == "POST":
		print(request.POST)
		return HttpResponse("OK!")
	return render(request, "test.html")
