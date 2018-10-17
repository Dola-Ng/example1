from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import template
from booklist.models import Booklist
import datetime



def index(request):
	loop = [0,1,2,3,4,5,6]
	booklist = Booklist.objects.all()
	book = request.POST.get('book',False)
	review = request.POST.get('review',False)	     
	date = datetime.datetime.now() 
	Booklist.objects.create( book=book, review=review, date=date)
	reviews = Booklist.objects.all()


	return render (request, 'html.html',{'booklist':booklist,'loop':loop,'book':book,'review':review,'date':date})
	

def page (request):
	return render (request, 'page.html')





		