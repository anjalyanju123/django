from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def Wishes(request):
    return HttpResponse('heyyyyyy you again')
def Wishes2(request):
    return HttpResponse('goood morning')
def std_name(request,a):
    return HttpResponse('student name'+a)
def std_age(request,b):
    return HttpResponse(f'student age{b}')

def Base_html(request):
    return render(request,'1_base.html')

def static(request):
    return render(request,'2_static.html')
def page_redirection_home(request):
    return render(request,'3.page_redirectionhome.html')
def page_redirection_about(request):
    return render(request,'4.page_redirectionabout.html')
def page_redirection_contact(request):
    return render(request,'5.page_redirectioncontact.html')

def extends_home(request):
    return render(request,'7.extendinghome.html')

def extends_about(request):
    return render(request,'7.extendingabout.html')

def extends_contact(request):
    return render(request,'7.extendingcontact.html')

def datatohtml(request):
    data = student.objects.all()
    return render(request,'10.database.html',{'Details':data})


def ormqueries(request):

   # 1. Create a new student record

    data = student.objects.create(name="John Doe", age=20, subject="Mathematics")
    return render(request,'11.ormqueries.html',{'Details': data})

def ormqueries2(request):

    # Retrieve a student by ID or return a 404 error if not found

    detail = student.objects.get(id=11)
    return render(request, '11.ormqueries.html', {'Details': detail})

def student_list(request):
    data = student.objects.all()
    return render(request,'15.ormqueries.html',{'Details': data})

def student_filter(request):
    data = student.objects.filter(age=18)
    return render(request,'15.ormqueries.html',{'Details': data})

def student_filter_update(request):
    data = student.objects.filter(id=8).update(name="June", age=20)
    return render(request,'11.ormqueries.html',{'Details': data})

def student_filter_delete(request):
    data = student.objects.filter(id=11).delete()
    return render(request,'11.ormqueries.html',{'Details': data})

def student_order(request):
    data = student.objects.all().order_by('age')
    return render(request,'15.ormqueries.html',{'Details': data})

def student_count(request):
    data = student.objects.count()
    context = {
          "total_students": data,
     }
    return render(request,'11.ormqueries.html',{'Details': data}, context)

def register(request):
    if request.method == 'POST':
        rform = Regform(request.POST)

        if rform.is_valid():
            n = rform.cleaned_data['name']
            p = rform.cleaned_data['phone']
            e = rform.cleaned_data['email']
            pwd = rform.cleaned_data['password']

            b = regmodel(Name=n, Phone=p, Email=e, Password=pwd)
            b.save()
            return redirect('/login')
        else:
            return HttpResponse('registration failed')
    else:
        return render(request,'13.reg.html')
    

def login(request):
    if request.method == 'POST':     
        lform = Logform(request.POST)

        if lform.is_valid():
            em = lform.cleaned_data['email']
            pwd = lform.cleaned_data['password']

            b = regmodel.objects.all()   

            for i in b:
                if em == i.Email and pwd == i.Password:
                    return HttpResponse('login succesfull')
                else:
                    return HttpResponse('failed to login')
        else:        
            return HttpResponse('invalid')              
        
    return render(request,'14.login.html')            