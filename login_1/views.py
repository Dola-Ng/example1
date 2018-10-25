
from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

def index_t(request):
    if request.user.is_authenticated:
        name = request.user.username
    return render(request,"index_t.html",locals())

def register_t(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		email = request.POST.get('email', False)

		try:
			user = User.objects.get(username=name)
		except:
			user = None
		if user is not None:
			message = 'The Name is Taken'
		else:
			user = User.objects.create_user(name, email, password)
			
			user.save()
			message = "Success"
			return render(request, "index_t.html", locals())
	return render(request, 'register_t.html', locals())

def login_t(request):
	if request.method == 'POST':   
		name = request.POST['username']   
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password) 
		if user is not None:         
			if user.is_active:
				auth.login(request,user)
				return redirect('/index_t/')  
				message = 'Success'
			else:
				message = 'User Not Found!'
		else:
			message = 'Log In Error'
	return render(request,"login_t.html",locals())  

def logout_t(request):
	auth.logout(request)  
	return redirect('/index_t/')