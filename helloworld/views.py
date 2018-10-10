from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import template
from booklist.models import Booklist


def index(request):
	loop = [0,1,2,3,4,5,6]
	


	booklist = Booklist.objects.all().order_by('date')
	return render (request, 'html.html',{'booklist':booklist,'container':loop})