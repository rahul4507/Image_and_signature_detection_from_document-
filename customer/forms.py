from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer


class CustomerRegisterForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('username','password1', 'password2')

    
class LoginForm(AuthenticationForm):
    pass