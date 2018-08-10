from rest_framework import serializers
from .models import Lesson, Validation, Confirmation

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields=('subject','paper')




class ValidationSerializer(serializers.ModelSerializer):
    """Your data serializer, define your fields here."""
    class Meta:
        model=Validation
        fields=("TransactionType","TransID","TransTime","TransAmount","BusinessShortCode", "BillRefNumber","InvoiceNumber","OrgAccountBalance","ThirdPartyTransID","MSISDN","FirstName","MiddleName","LastName")


class ConfirmationSerializer(serializers.ModelSerializer):
    """Your data serializer, define your fields here."""
    class Meta:
        model=Confirmation
        fields=("TransactionType","TransID","TransTime","TransAmount","BusinessShortCode", "BillRefNumber","InvoiceNumber","OrgAccountBalance","ThirdPartyTransID","MSISDN","FirstName","MiddleName","LastName")









    # TransactionType= serializers.CharField(required=False, max_length=100, allow_blank=True)
    # TransID:serializers.CharField(required=False, max_length=100, allow_blank=True)
    # TransTime=serializers.CharField(required=False, max_length=100, allow_blank=True) 
    # TransAmount=serializers.CharField(required=False, max_length=100, allow_blank=True) 
    # BusinessShortCode=serializers.CharField(required=False, max_length=100, allow_blank=True)
    # BillRefNumber=serializers.CharField(required=False, max_length=100, allow_blank=True)
    # InvoiceNumber=serializers.CharField(required=False, max_length=100, allow_blank=True)   
    # OrgAccountBalance=serializers.CharField(required=False, max_length=100, allow_blank=True) 
    # ThirdPartyTransID=serializers.CharField(required=False, max_length=100, allow_blank=True)
    # MSISDN=serializers.CharField(required=False, max_length=100, allow_blank=True)
    # FirstName=serializers.CharField(required=False, max_length=100, allow_blank=True)
    # MiddleName=serializers.CharField(required=False, max_length=100, allow_blank=True)     
    # LastName=serializers.CharField(required=False, max_length=100, allow_blank=True)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Validation.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.TransactionType = validated_data.get('TransactionType', instance.TransactionType)
    #     instance.TransID = validated_data.get('TransID', instance.TransID)
    #     instance.TransTime = validated_data.get('TransTime', instance.TransTime)
    #     instance.TransAmount = validated_data.get('TransAmount', instance.TransAmount)
    #     instance.BusinessShortCode = validated_data.get('BusinessShortCode', instance.BusinessShortCode)
    #     instance.BillRefNumber = validated_data.get('BillRefNumber', instance.BillRefNumber)
    #     instance.InvoiceNumber = validated_data.get('InvoiceNumber', instance.InvoiceNumber)
    #     instance.OrgAccountBalance = validated_data.get('OrgAccountBalance', instance.OrgAccountBalance)
    #     instance.ThirdPartyTransID = validated_data.get('ThirdPartyTransID', instance.ThirdPartyTransID)
    #     instance.MSISDN = validated_data.get('MSISDN', instance.MSISDN)
    #     instance.FirstName = validated_data.get('FirstName', instance.FirstName)
    #     instance.MiddleName = validated_data.get('MiddleName', instance.MiddleName)
    #     instance.LastName = validated_data.get('LastName', instance.LastName)
                                
                        

    #     instance.save()
    #     return instance
    


   

