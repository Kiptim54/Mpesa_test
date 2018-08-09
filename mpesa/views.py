# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class mpesaAPIView(APIView):
    def post(requests, *args,**kwargs):
        return render(request )
    
