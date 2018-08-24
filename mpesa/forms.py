from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(max_length=20, required=False, label="First Name")
    last_name=forms.CharField(max_length=20,required=False, label="Last Name")
    phone_number = forms.CharField(help_text='Required. Format: +254')
    


    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number','password1', 'password2',)


