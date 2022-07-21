from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = { 'username': forms.TextInput(attrs={
            'class':'form-control',
            'type': "text",
            'id': "floatingInput",
            'placeholder':"Username",}),
                    'password':forms.PasswordInput(attrs={
            'class':'form-control',
            'type': "password",
            'id': "floatingPassword",
            'placeholder':"Password"})
            }

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = { 'username': forms.TextInput(attrs={
            'class':'form-control',
            'type':'text',
            'placeholder':'Username',
            'id': "floatingInput",}),
                    'email': forms.EmailInput(attrs={
            'class':'form-control',
            'type':'email',
            'placeholder':'Email',
            'id': "floatingEmail",}),
                    'password1':forms.PasswordInput(attrs={
            'class':'form-control',
            'type': "password",
            'id': "floatingPassword",
            'placeholder':"Password"}),
                    'password2':forms.PasswordInput(attrs={
            'class':'form-control',
            'type': "password",
            'id': "floatingPassword",
            'placeholder':"Password again"
                    })}

