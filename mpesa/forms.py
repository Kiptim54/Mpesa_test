from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(max_length=20, required=False, label="First Name")
    last_name=forms.CharField(max_length=20,required=False, label="Last Name")
    # Phone_Number=PhoneNumberField(label="Phone Number +254")
    phone_number=forms.IntegerField()
    


    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number','password1', 'password2',)

    
# class Student_Signup(forms.ModelForm):
#     """
#     This a signup form
#     """
#     class Meta:
#         model = User
#         fields =['username','first_name','last_name','email','password1','password2',]
#         widgets = {
#             'username': forms.TextInput(attrs={'required': True}),
#             'phone_number': forms.TextInput(attrs={'required': True}),
#             'country': forms.TextInput(attrs={'required': True}),
#             'county': forms.TextInput(attrs={'required': True}),
#             'school': forms.TextInput(attrs={'required': True}),

#         }