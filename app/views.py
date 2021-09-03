from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect
from app.models import place
# Create your views here.

def demo(request):
    return render(request,"refresh.html")

def refresh(request):
    obj = place.objects.all()
    return render(request,"refresh.html",{'result':obj})

def logout(request):
    return render(request,"index.html")


