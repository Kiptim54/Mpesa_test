from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(max_length=20, required=False, label="First Name")
    last_name=forms.CharField(max_length=20,required=False, label="Last Name")
    Phone_Number=forms.IntegerField(label="Phone Number +254")

    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'Phone_Number', 'email','password1', 'password2',)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.Phone_Number = self.cleaned_data["Phone_Number"]
        if commit:
            user.save()
        return user