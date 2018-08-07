# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login


def index(request):
    title="Home Page"
    current_user = request.user
    try:
        print(current_user.profile.phone_number)
    except:
        print("anonymous")
    return render(request, 'index.html', {"title":title})


# def SignUp(request):
#     '''
#     User sign up with additional fields First Name, Last Name
#     and Phone Number 
#      '''
#     title= "SignUp | eLimu"
#     if request.method=='POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.refresh_from_db()
#             user.profile.Phone_Number=form.cleaned_data.get('phone_number')
#             print(user.profile.Phone_Number)
#             print("hey")
#             user.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user= authenticate(username=username, password=raw_password)
#             login(request,user)
            
#             print("hey");
#             return redirect('index_page')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {"title":title, "form":form})


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            print("hello from here")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index_page')
    else:
        form = SignUpForm()
        print("failing")
    return render(request, 'registration/signup.html', {'form': form})