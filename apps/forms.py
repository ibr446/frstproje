from django.contrib.auth.models import User
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users
from django.forms import ModelForm



class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

