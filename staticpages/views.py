from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, Context, loader

# Create your views here.
def index(request):
	context = RequestContext(request, {})
	template = loader.get_template('index.html')
	return HttpResponse(template.render(
		context,
		request
	))

def login(request):
	if request.method == 'GET':
		return redirect('/');

	if request.method == 'POST':
		context = RequestContext(request, {
		"username": request.POST.get('username', ''),
		"password": request.POST.get('password', '')})
		template = loader.get_template('login.html')
		return HttpResponse(template.render(
			context,
			request,
		))
