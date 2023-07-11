from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
import re

def home(request):
    return render(request,'index.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        splitted_name = fullname.split()
        try:
           myuser = User.objects.create_user(username,email,pass1)
        except IntegrityError:
           messages.error(request,'Username already exists')
           return redirect('home')
        
    
        myuser.first_name= splitted_name[0]
        myuser.last_name= splitted_name[-1]

        domain = email.split('@')[1]
        valid_domains = ['gmail.com', 'yahoo.com','ncit.edu.np']
        if domain not in valid_domains:
            messages.error(request,'Invalid email')
            return redirect('home')
        
        if len(pass1) < 8 or not re.match(r'^[A-Za-z0-9@#$%^&+=]+$', pass1):
           messages.error(request," Password must be at least 8 characters long and contain special character!")
           return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,'Passwords did not match!')
            return redirect('home')
        else:
            myuser.save()
            messages.success(request, "Signed up successfully!")
            return redirect('home')
    else:
        return HttpResponse('404 -Not Found!')
    

def signin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            messages.success(request,'Logged in successfully!')           
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials!')
            return redirect('home')
    return redirect('home')

def signout(request):
    logout(request)
    messages.success(request,'Signed out successfully!')
    return redirect('home')

def qna_section(request):
    return HttpResponse("Oops! We are working on it:(")