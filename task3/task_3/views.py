from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages, auth


# Create your views here.

def user_input(request):
    if request.method == 'POST':

        if ProfileForm(request.POST).is_valid():
            nm = ProfileForm(request.POST).cleaned_data['name']
            ad = ProfileForm(request.POST).cleaned_data['address']
            em = ProfileForm(request.POST).cleaned_data['email']
            ph = ProfileForm(request.POST).cleaned_data['phone']

            b = ProfileModel(Name=nm, Email=em, Address=ad, Phone=ph)
            b.save()

            return redirect('/Profile')
        else:
            return HttpResponse('Failed')

    return render(request, 'input.html')
        
def Profile(request):
    data = ProfileModel.objects.all()
    return render(request, 'Profile_card.html', {'profile': data})

def Profile_2(request):
    data = Profile2Model.objects.all()
    return render(request, 'Profile_2.html', {'profile': data})

def homepage(request):
    return render(request,'home.html')

def authregister(request):
    if request.method == 'POST':
        rform = Profile2Form(request.POST, request.FILES)  # Handle file uploads

        if rform.is_valid():
            # Extract the form data
            e = request.POST['email']
            p = request.POST['password']
            rp = request.POST['re-password']

            # These are the profile-specific fields
            fn = rform.cleaned_data['first_name']
            ln = rform.cleaned_data['last_name']
            ad = rform.cleaned_data['address']
            ph = rform.cleaned_data['phone']
            ag = rform.cleaned_data['age']
            up = rform.cleaned_data['upload']

            # Check if passwords match
            if p == rp:
                if User.objects.filter(email=e).exists():
                    messages.error(request, 'Email already exists.')
                else:
                    # Create the User object
                    user = User.objects.create_user(username=e, email=e, password=p)
                    user.save()

                    # Create the Profile2Model instance and link it to the user
                    profile = Profile2Model(first_name=fn, last_name=ln, address=ad, phone=ph, age=ag, upload=up)
                    profile.save()

                    messages.success(request, 'Registration completed successfully.')
                    return redirect('/authlogin')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Form is invalid, please correct the errors.')

    else:
        rform = Profile2Form()

    return render(request, 'register.html', {'profile': profile})

def authlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Complete')
            return redirect('/Profile_2') 
        else:
            messages.error(request, 'Invalid Login')
    return render(request, 'login.html')  

def authlogout(request):
    logout(request) 
    return redirect('/homepage') 

def book_list(request):
    book = Book.objects.all()
    return render(request,'Booklist.html',{'Book':book})

def add_book(request):
    if request.method == 'POST':
        form = Bookform(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/book_list')
    else:
        form = Bookform()
    return render(request, 'Add_book.html',{'form':form})   