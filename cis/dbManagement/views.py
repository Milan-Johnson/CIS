from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Student, Faculty
#from .filters import StudentFilter

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def search_details(request):
    # qs = Student.objects.all()
    name_query = request.GET.get('search_name')
    year_query  = request.GET.get('year')
    dept_query = request.GET.get('department')
    cat_query = request.GET.get('category')

    # name = request.GET.get('name')
    #print(name)
    if cat_query:
        qs = Student.objects.all()
    else:
       qs = Faculty.objects.all() 

    
    if year_query != '' and name_query is not None:
        qs = qs.filter(yearOfAddmission__icontains=year_query)
    if name_query != '' and name_query is not None:
        qs = qs.filter(name__icontains=name_query)
    if dept_query != '' and name_query is not None:
        qs = qs.filter(department__icontains=dept_query)
    
    context = {
        'queryset' : qs 
    }
    print(context)
    return render(request, "bootstrap_form.html",context)