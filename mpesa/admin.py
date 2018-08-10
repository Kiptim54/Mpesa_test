# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Lesson, Validation


admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(Validation)