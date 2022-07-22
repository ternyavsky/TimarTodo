from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django.forms import CheckboxInput, ModelForm, TextInput
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

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','complete']
        widgets = {
                'title': TextInput(attrs={
                        'class':'form-control w-100 mt-2',
                        'type':'search',
                        'placeholder':'Walk the dog...',
                        'aria-label':'Search'}),
                'complete':CheckboxInput(attrs={
                        'class':"form-check-input",
                        'type':"checkbox", 
                        'value ': "", 
                        'id':"flexCheckDefault"
                })
                }
   

