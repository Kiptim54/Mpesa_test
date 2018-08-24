# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from .models import Profile, Lesson
from .serializers import(
     LessonSerializer,
    #  ConfirmationSerializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class OnlinePaymentAPIView(APIView):
    """
    """
    def post(self,request,*args,**kwargs):
        BusinessShortCode=request.data["BusinessShortCode"]
        Password= request.data["password"]
        Timestamp= request.data["Timestamp"]
        CheckoutRequestID= request.data["CheckoutRequestID"]


        data = {
            "BusinessShortCode":BusinessShortCode,
            "password":password,
            "Timestamp":Timestamp,
            "CheckoutRequestID":CheckoutRequestID
        }
        OnlinePaymentcreate_seriliazer = OnlinePaymentSeriliazer(data=data)
        if OnlinePaymentcreate_seriliazer.is_valid():
            new_payment = OnlinePaymentcreate_seriliazer.save()

            success_response ={
                "MerchantRequestID":MerchantRequestID,
                "CheckoutRequestID":CheckoutRequestID,
                "ResponseCode":ResponseCode,
                "ResultDesc":ResultDesc,
                "ResponseDescription":ResponseDescription,
                "ResultCode":ResultCode
            }
            return Response(success_response, status=status.HTTP_200_OK)
        return Response(OnlinePaymentcreate_serializer.errors,status=HTTP_400_BAD_REQUEST)

        
   


# class ConfirmationAPIView(APIView):
    
#     """
    
#     """
#     def post(self,request,*args,**kwargs):

#         TransactionType = request.data["TransactionType"]
#         TransID = request.data["TransID"]
#         TransTime = request.data["TransTime"]
#         TransAmount = request.data["TransAmount"]
#         BusinessShortCode = request.data["BusinessShortCode"]
#         BillRefNumber = request.data["BillRefNumber"]
#         InvoiceNumber = request.data["InvoiceNumber"]
#         OrgAccountBalance = request.data["OrgAccountBalance"]
#         ThirdPartyTransID = request.data["ThirdPartyTransID"]
#         MSISDN = request.data["MSISDN"]
#         FirstName = request.data["FirstName"]
#         MiddleName = request.data["MiddleName"]
#         LastName = request.data["LastName"]
        



#     data={

#         "TransactionType":TransactionType,
#         "TransID":TransID,
#         "TransTime":TransTime,
#         "TransAmount":TransAmount,
#         "BusinessShortCode":BusinessShortCode,
#         "BillRefNumber":BillRefNumber,
#         "InvoiceNumber":InvoiceNumber,
#         "OrgAccountBalance":OrgAccountBalance,
#         "ThirdPartyTransID":ThirdPartyTransID,
#         "MSISDN":MSISDN,
#         "FirstName":FirstName,
#         "MiddleName":MiddleName,
#         "LastName":LastName
#     }
#     confirmationcreate_seriliazer= ConfirmationSerializer(data=data)
#     if confirmationcreate_serializer.is_valid():
#         new_confirmation = confirmationcreate_serializer.save()
    #     success_response={
    #         "ConversationID": "",
	#         "OriginatorCoversationID": "",
	#         "ResponseDescription": "success"
    #         }
       
    #     return Response(success_response,status=status.HTTP_200_OK)
    # return Response(confirmationcreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)






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
    
