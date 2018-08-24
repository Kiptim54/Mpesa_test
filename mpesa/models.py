# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mpesa_api.util.managers import AuthTokenManager




class AuthToken(models.Model):
    """Handles AuthTokens"""
    access_token = models.CharField(max_length=40);
    type = models.CharField(max_length=3)
    expires_in = models.BigIntegerField()
    objects = AuthTokenManager()

    def __str__(self):
        return self.access_token

    class Meta:
        db_table ='tbl_access_token'
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
# Create your models here.
# class C2BRequest(models.Model):
#     """ 
#     Handles C2B Requests
#     """

#     TransactionType = models.IntegerField()
#     TransID = models.IntegerField()
#     TransTime = models.IntegerField()
#     BusinessShortCode = models.IntegerField()
#     BillRefNumber = models.IntegerField()
#     InvoiceNumber =models.IntegerField()
#     OrgAccountBalance = models.IntegerField()
#     ThirdPartyTransID =models.CharField(max_length=90) 
#     MSISDN = models.IntegerField()
#     FirstName = models.CharField(max_length=80)
#     MiddleName = models.CharField(max_length=80)
#     LastName = models.CharField(max_length=80)



#     def __str__(self):
#         return str(self.TransactionType)
        
    # id = models.BigAutoField(primary_key=True)
    # transaction_type = models.CharField(max_length=20, blank=True, null=True)
    # transaction_id = models.CharField(max_length=20, unique=True)
    # transaction_date = models.DateTimeField(blank=True, null=True)
    # amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # business_short_code = models.CharField(max_length=20, blank=True, null=True)
    # bill_ref_number = models.CharField(max_length=50, blank=True, null=True)
    
    # third_party_trans_id = models.CharField(max_length=50, blank=True, null=True)
    # phone = models.BigIntegerField(blank=True, null=True)
    # first_name = models.CharField(max_length=50, blank=True, null=True)
    # middle_name = models.CharField(max_length=50, blank=True, null=True)
    # last_name = models.CharField(max_length=50, blank=True, null=True)
    # is_validated = models.BooleanField(default=False)
    # is_completed = models.BooleanField(default=False)
    # date_added = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

    # class Meta:
    #     db_table ='tbl_c2b_requests'
    #     verbose_name_plural = 'C2B Requests'

    # @property
    # def name(self):
    #     return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)





class OnlineCheckout(models.Model):
    """
    Handles Online Checkout
    """
    id = models.BigAutoField(primary_key=True)
    phone = models.BigIntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    checkout_request_id = models.CharField(max_length=50, default='')
    account_reference = models.CharField(max_length=50, default='')
    transaction_description = models.CharField(max_length=50, blank=True, null=True)
    customer_message = models.CharField(max_length=100, blank=True, null=True)
    merchant_request_id = models.CharField(max_length=50, blank=True, null=True)
    response_code = models.CharField(max_length=5, blank=True, null=True)
    response_description = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone)

    class Meta:
        db_table = 'tbl_online_checkout_requests'
        verbose_name_plural = 'Online Checkout Requests'


class OnlineCheckoutResponse(models.Model):
    """
    Handles Online Checkout Response
    """
    id = models.BigAutoField(primary_key=True)
    merchant_request_id = models.CharField(max_length=50, blank=True, null=True)
    checkout_request_id = models.CharField(max_length=50, default='')
    result_code = models.CharField(max_length=5, blank=True, null=True)
    result_description = models.CharField(max_length=100, blank=True, null=True)
    mpesa_receipt_number = models.CharField(max_length=50, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone)

    class Meta:
        db_table = 'tbl_online_checkout_responses'
        verbose_name_plural = 'Online Checkout Responses'

class OnlinePayment(models.Model):
    """
    check the status of a Lipa Na M-Pesa Online Payment
    """
    BusinessShortCode = models.PositiveIntegerField(default=0)
    Password =models.CharField(max_length=60)
    Timestamp = models.DateTimeField(auto_now=True)
    CheckoutRequestID =models.CharField(max_length=90)

    def __str__(self):
        return str(self.BusinessShortCode)



















