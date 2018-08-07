# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from .models import Profile


def index(request):
    title="Home Page"
    current_user = request.user
    try:
        profile=Profile.objects.get(user=current_user)
        return render(request, 'index.html', {"title":title,"profile":profile})
    except:
        print("anonymous user")
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
            user=form.save()
            user.refresh_from_db()
            user.profile.phone_number=form.cleaned_data.get('phone_number')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('index_page')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {"title":title, "form":form})


