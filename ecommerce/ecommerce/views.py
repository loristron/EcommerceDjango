from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
	template_name = 'home_page.html'
	context		  = {'page_title': "Home Page", }
	return render(request, template_name, context)
