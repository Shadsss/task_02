from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
	context = {
	"msg":"Hello World!"
	}
	return render(request, 'restaurants.html', context)