from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import template
from booklist.models import Booklist
from django.template.loader import get_template 
import datetime



def index(request):
	loop = [0,1,2,3,4,5,6]
	booklist = Booklist.objects.all()
	bookname = request.POST.get('bookname',False)
	review = request.POST.get('review',False)	     
	date_time = datetime.datetime.now() 
	new = Booklist.objects.create(bookname=bookname, review=review, date_time=date_time)
	reviews = Booklist.objects.all()


	return render (request, 'html.html',{'booklist':booklist,'loop':loop,'bookname':bookname,'review':review,'date_time':date_time})
	

def page (request):
	return render (request, 'page.html')





		