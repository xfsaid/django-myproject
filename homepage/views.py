#coding:utf-8
import json
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from .models import TeacherInfo



# Create your views here.
def welcome(request):
    st = loadjsonfile()
    return HttpResponse(u"%s" % st)

def index(request):
    tec_info_list_all = TeacherInfo.objects.all()
    paginator = Paginator(tec_info_list_all, 3)
    page = request.GET.get('page')

    try:
        tec_info_list = paginator.page(page)
    except PageNotAnInteger:
        tec_info_list = paginator.page(1)
    except EmptyPage:
        tec_info_list = paginator.page(paginator.num_pages)
    return render_to_response('index.html',{'tec_info_list':tec_info_list})


def loadjsonfile():
    j_f = open("jsonfiles/tabs.json",'r')
    tabs = json.load(j_f)
    family = tabs['fontSize']
    return family['2']