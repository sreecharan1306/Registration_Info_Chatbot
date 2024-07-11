from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.cotrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password']