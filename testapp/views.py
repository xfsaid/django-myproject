from django.shortcuts import render,render_to_response,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django import forms
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from homepage.models import TeacherInfo
from .models import User



# Create your views here.
def listing(request):
    contact_list = TeacherInfo.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page
 
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
 
    return render(request, 'list.html', {'contacts': contacts})


class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

@csrf_exempt
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']

            user = User()
            user.username = username
            user.headimg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    #c = RequestContext(request,{
    #    'uf':uf,
    #})
    #return render_to_response('register.html', c)
    return render_to_response('register.html', RequestContext(request,{'uf':uf,}))