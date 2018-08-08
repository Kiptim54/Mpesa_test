# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Account_Balance = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=40 ,null=True, blank=True)

    def __str__(self):
        return self.user.username
        

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Lesson(models.Model):
    subject=models.CharField(max_length=40)
    paper=models.CharField(max_length=40)
    purchased=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject