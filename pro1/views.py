#-*-coding:utf-8-*-

from django.template import RequestContext
from django.shortcuts import render

def index(request):
	return render(request,'index.html')
