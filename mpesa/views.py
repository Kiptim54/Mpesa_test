# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login


def index(request):
    title="Home Page"
    current_user = request.user
    return render(request, 'index.html', {"title":title})


def SignUp(request):
    '''
    User sign up with additional fields First Name, Last Name
    and Phone Number 
     '''
    title= "SignUp | eLimu"
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            login(request,user)
            
            print("hey");
            return redirect('index_page')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {"title":title, "form":form})
