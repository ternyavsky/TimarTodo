from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegistrationForm
# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'

class SupportView(TemplateView):
    template_name = 'main/support.html'

class ExamplesView(TemplateView):
    template_name = 'main/examples.html'

#Login Views
class LoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

class RegistrationView(CreateView):
    template_name = 'registration/register.html' 
    form_class = RegistrationForm
    success_url = 'accounts/login'

class ProfileView(TemplateView):
    template_name = 'main/profile.html'


