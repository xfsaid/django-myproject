#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import TeacherInfo


# Create your views here.
def welcome(request):
    return HttpResponse("欢迎")

def index(request):
    tec_info_list = TeacherInfo.objects.all()
    return render_to_response('index.html',{'tec_info_list':tec_info_list})