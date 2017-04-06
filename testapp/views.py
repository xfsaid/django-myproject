from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from homepage.models import TeacherInfo
# Create your views here.
def listing(request):
    contact_list = TeacherInfo.objects.all()
    paginator = Paginator(contact_list, 1) # Show 25 contacts per page
 
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