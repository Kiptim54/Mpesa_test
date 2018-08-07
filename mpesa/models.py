# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField



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