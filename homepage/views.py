#coding:utf-8
import json
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from .models import Teacher,GradeSubject



# Create your views here.
def welcome(request):
    st = loadjsonfile()
    return HttpResponse(u"%s" % st)

def index(request):
    if request.user.is_authenticated():
        logged_username = request.user
            
    grade_level = request.GET.get('grade_level','gradefirst')
    subject_level = request.GET.get('subject_level','chinese')

    tec_info_list_all = []
    for tec_info in Teacher.objects.all():
        if not subject_level == tec_info.skill2.slug:
            continue
        for ti in tec_info.skill.all():
            if grade_level == ti.slug:
                tec_info_list_all.append(tec_info)
                break

    paginator = Paginator(tec_info_list_all, 3)
    page = request.GET.get('page')
    try:
        tec_info_list = paginator.page(page)
    except PageNotAnInteger:
        tec_info_list = paginator.page(1)
    except EmptyPage:
        tec_info_list = paginator.page(paginator.num_pages)

    grade_subject_info = GradeSubject.objects.all()
    # return render_to_response('index.html',{
    #    'tec_info_list':tec_info_list,
    #    'grade_subject_info':grade_subject_info})
    return render_to_response('index.html',locals())


def loadjsonfile():
    j_f = open("jsonfiles/tabs.json",'r')
    tabs = json.load(j_f)
    family = tabs['fontSize']
    return family['2']