from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_pages_view(request):
	return HttpResponse("Hola mundo!!!")
