# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name')
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Profile)