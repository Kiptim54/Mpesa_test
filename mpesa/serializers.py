from rest_framework import serializers
from .models import (
    Lesson
    # C2BRequest
    )
from rest_framework.serializers import(
    CharField,
    IntegerField
    
)

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields=('subject','paper')




class  OnlinePaymentSeriliazer(serializers.ModelSerializer):
    """
    This is OnlinePaymentSeriliazer
    """
    class Meta:
        model =OnlinePayment 
        fields =(
            'BusinessShortCode',
            'Password',
            'Timestamp',
            'CheckoutRequestID'
          
        )
        def create(self,validated_data):
            """
            This is the original data passed from the request
            """
            onlinepayment = OnlinePayment(
                BusinessShortCode = validated_data['BusinessShortCode'],
                # Password = validated_data['Password '],
                Timestamp = validated_data['Timestamp'],
                CheckoutRequestID = validated_data['CheckoutRequestID']
               
            )
            onlinepayment.set_password(validated_data[password])
            onlinepayment.save()
            return onlinepayment



# class ConfirmationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = C2BRequest
#         fields =(
#             'TransactionType',
#             'TransID',
#             'TransTime',
#             'BusinessShortCode',
#             'BillRefNumber',
#             'InvoiceNumbe',
#             'OrgAccountBalance',
#             'ThirdPartyTransID',
#             'FirstName',
#             'MiddleName',
#             'LastName'

#         )
#         def create(self,validated_data):
#             new_created_confirmation = C2BRequest(
#                 TransactionType=validated_data['TransactionType'],
#                 TransID = validated_data['TransID'],
#                TransTime = validated_data['TransTime'],
#                BusinessShortCode = validated_data['BusinessShortCode'],
#                 BillRefNumber = validated_data['BillRefNumber'],
#                 InvoiceNumber = validated_data['InvoiceNumber'],
#                 OrgAccountBalance =validated_data['OrgAccountBalance'],
#                 ThirdPartyTransID =validated_data['ThirdPartyTransID'], 
#                 FirstName=validated_data['FirstName'],
#                 MiddleName =validated_data['MiddleName'],
#                 LastName = validated_data['LastName']

#             )
            
#             # new_created_teacher.set_password(validated_data['password'])
#             new_created_confirmation.save()
#             return new_created_confirmation

    # TransactionType = serializers.IntegerField()
    # TransID = serializers.IntegerField()
    # TransTime = serializers.IntegerField()
    # BusinessShortCode = serializers.IntegerField()
    # BillRefNumber = serializers.IntegerField()
    # InvoiceNumber =serializers.IntegerField()
    # OrgAccountBalance = serializers.IntegerField()
    # ThirdPartyTransID =serializers.CharField() 
    # MSISDN = serializers.IntegerField()
    # FirstName = serializers.CharField(max_length=80)
    # MiddleName = serializers.CharField(max_length=80)
    # LastName = serializers.CharField(max_length=80)
        


    
    