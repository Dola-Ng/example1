from django.shortcuts import render,redirect, render_to_response  # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from django import template

import datetime

#from django.contrib.auth.forms import UserCreationForm
#from login_1.models import register

def index(request):
	return render (request, 'index.html',locals())

def calligraphy(request):
	return render (request, 'calligraphy.html',locals())

def store(request):
	return render (request, 'store.html',locals())

def journal(request):
	return render (request, 'journal.html',locals())

def website(request):
	return render (request, 'website.html',locals())

def colorgame(request):
	return render (request, 'color.html',locals())

def museum(request):
	return render (request, 'museum.html',locals())

def scorekeeper(request):
	return render (request, 'scorekeeper.html',locals())


