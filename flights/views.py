from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, Flight

# Create your views here.

"""
def Hello(request):
	return HttpResponse("Hello, world!")
"""

def index(request):
	context = {
		"airports": Airport.objects.all()
	}
	return render(request, "flights/index.html", context)
