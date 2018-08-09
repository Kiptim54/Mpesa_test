# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from .models import Profile, Lesson
from .serializers import LessonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


def index(request):
    title="eLimu | Home page"
    current_user = request.user
    lessons=Lesson.objects.all()
    try:
        profile=Profile.objects.get(user=current_user)
        return render(request, 'index.html', {"title":title,"profile":profile,"lessons":lessons})
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


class LessonList(APIView):
    def get(self, request, format=None):
        all_lessons = Lesson.objects.all()
        serializers = LessonSerializer(all_lessons, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers=LessonSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class mpesaAPIView(APIView):
    def post(requests, *args,**kwargs):
        return render(request )
    
