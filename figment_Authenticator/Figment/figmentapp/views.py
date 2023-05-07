from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from figmentapp.models import Contact 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'aboutus.html')

def scanner(request):
    return render(request, 'employeeScanner.html')

def admin_login(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password1 = request.POST.get('password')
         user = authenticate(request, username=username, password=password1)
         if user is not None:
              login(request, user)
              return redirect('admin_dashboard')
         else:
              return HttpResponse("Username and Password are incorrect!!!")
    return render(request, 'adminlogin.html' )

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date= datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
    return render(request, 'contact.html')

def new_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Your password and confirm password are not same!!!")
        else:
            my_user = User.objects.create_user(username, email,password1)
            my_user.save()
            return redirect('admin_login')
    return render(request, 'adminRegistration.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):
       return render(request, 'adminDashboard.html')

@login_required(login_url='admin_login')
def new_employee(request):
       return render(request, 'registrationForm.html')
# def index(request):
#     return HttpResponse("this is home page")
def LogoutPage(request):
       logout(request)
       return redirect('admin_login')
