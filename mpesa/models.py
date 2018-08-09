# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class C2BRequest(models.Model):
    """
    Handles C2B Requests
    """
    id = models.BigAutoField(primary_key=True)
    transaction_type = models.CharField(max_length=20, blank=True, null=True)
    transaction_id = models.CharField(max_length=20, unique=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    business_short_code = models.CharField(max_length=20, blank=True, null=True)
    bill_ref_number = models.CharField(max_length=50, blank=True, null=True)
    
    third_party_trans_id = models.CharField(max_length=50, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_validated = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

    class Meta:
        db_table ='tbl_c2b_requests'
        verbose_name_plural = 'C2B Requests'

    @property
    def name(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)
