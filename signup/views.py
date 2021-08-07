from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect


# Create your views here.

def signup(request):
    if request.method == 'POST':

    #user account adding
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confpassword = request.POST['confpassword']

    # password matching alert
        if  password==confpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Exist")
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exist")
                return redirect('signup')

            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"password mismatch")
            return redirect('signup')

        return redirect('/')

    return render(request,"sign-up.html")

def login(request):
    if request.method == 'POST':

    #user account adding
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        # user.save()
        # print("user login")

        if user is not None:
            auth.login(request,user)
            return redirect('refresh')
        else:
            messages.info(request,"invalid login")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('refresh')