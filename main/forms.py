from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import City, Task
from django.forms import CharField, CheckboxInput, EmailInput, ModelForm, TextInput


class CusPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",
        'class':'form-control',
        'placeholder':'name@example.com',
        'type':'email'}),
    )

class CusPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            'class':'form-control',
            'type':'password',
            'placeholder':'Password',
            'id': "floatingPassword",}),
        
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
            'class':'form-control',
            'type':'password',
            'placeholder':'Password again',
            'id': "floatingPassword",}),
    )


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']
        widgets = { 'city':forms.TextInput(attrs={ 'class':'form-control',
                                             'name':'city',
                                             'placeholder':'Moscow...',
                                             'type':'text'  })}


class ChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        widgets = {
                'username': forms.TextInput(attrs={
                        'class':"form-control",
                        'type':"text",
                        'name':'username',
                        
        }),
                'email': forms.EmailInput(attrs={
                        'class':"form-control",
                        'type':"email",
                        'name':'email'}),
                'first_name': forms.TextInput(attrs={
                        'class':"form-control",
                        'type':"text",
                        'name':'first_name' 
                        }),
                'last_name': forms.TextInput(attrs={
                        'class':"form-control",
                        'type':"text",
                        'name':'last_name' 
                })
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "floatingInput",
        'placeholder':"Username",
        'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "current-password",
        'class':'form-control',
        'type': "password",
        'id': "floatingPassword",
        'placeholder':"Password",
        'name':'password'}),
    ) 
    
class ResetPassword(PasswordResetForm):
    email = forms.EmailField(
        
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'class':'form-control',
            'type':'email',
            'placeholder':'name@example.com',
            'name':'email',
            'id':'floatingInput'}),
    )

class RegistrationForm(UserCreationForm):

    email = CharField(widget=forms.EmailInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "email",
        'id': "floatingInput",
        'placeholder':"admin@admin.ru",
        'name':'email'}))
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "floatingInput",
        'placeholder':"Username",
        'name':'username'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "floatingPassword",
        'placeholder':"Password",
        'name':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "floatingPassword",
        'placeholder':"Password again",
        'name':'password2'
    }))

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
            'id': "floatingEmail",})}

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


   

