# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Lesson,OnlinePayment


admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(OnlinePayment)
