from django.shortcuts import render,render_to_response,HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.views import login, logout

# Create your views here.

#class UserForm(forms.Form):

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse(' ok!')
    else:
        form = UserCreationForm()
    return render_to_response('register.html', RequestContext(request,{'form': form,}))

def login_view(request):
    #request.GET['redirect_field_name'] = '/index'
    return login(request)

def logout_view(request):
    return logout(request)#logged_out.html???
    #return logout(request,'/index')
    #return logout(request,'/','registration/login.html')

# @csrf_exempt
# def login_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Correct password, and the user is marked "active"
#         auth.login(request, user)
#         # Redirect to a success page.
#         return HttpResponseRedirect("login.html")
#     else:
#         # Show an error page
#         return HttpResponseRedirect("login.html")

# @csrf_exempt
# def logout_view(request):
#         auth.logout(request)
#     # Redirect to a success page.
#     return HttpResponseRedirect("logout.html"")