from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
import requests
from django.contrib.auth import authenticate, login, logout
from main.models import Task
from .forms import *
# Create your views here.

class CustomPasswordReset(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = CusPasswordResetForm

class CustomPasswordConfirm(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = CusPasswordConfirmForm
    success_url = reverse_lazy('login')

class IndexView(TemplateView):
    template_name = 'main/index.html'

class SupportView(TemplateView):
    template_name = 'main/support.html'

class ExamplesView(TemplateView):
    template_name = 'main/examples.html'


def weather(request):
    key = '9fa3767c8c72bdd4a47e7c82897e6841'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key

    all_city = []

    responce = requests.get(url.format('Lipetsk')).json()
    city_info = {

            'temp': responce["main"]["temp"],
            'icon': responce["weather"][0]["icon"],

        }


    all_city.append(city_info)

    return render(request,'main/profile.html', {})




def deleteprofile(request,id):

    user = User.objects.get(id=id)
    user.delete()
    return redirect ('/')

def reset_password(request):
    form = ResetPassword()
    return render(request,'registration/password_reset_form.html',{'form':form})


def tasklist(request):


    objects = Task.objects.filter(author = request.user)

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('tasklist')

    context = { 'objects': objects, 'form':form}

    return render(request,'examples/tasklist.html', context)

def delete(request,id):
    try:
        object = Task.objects.get(id=id)
        object.delete()
        return redirect('tasklist')
    except:
        return HttpResponseNotFound ("<img src='https://http.cat/400'>")




def edit(request, id):
    try:
        user = User.objects.get(id=id)
        form = ChangeForm(instance=request.user)

        if request.method == "POST":
            user.username = request.POST.get("username")
            user.email = request.POST.get("email")
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            return redirect('profile',user.id)
        else:
            context = {'user':user,
                        'form':form}
            return render(request, "main/changeinfo.html", context)
    except User.DoesNotExist:
        return HttpResponseNotFound("<img src='https://http.cat/403'>")


def deleteall(request):
    objects = Task.objects.filter(author_id = request.user)
    objects.delete()
    return redirect('tasklist')

class TaskListView(ListView):
    template_name = 'examples/tasklist.html'
    model = Task


#Login Views
def loginview(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile',user.id)
        else:
            messages.success(request,'No valid login username or password!')



    context = {'form':form}
    return render(request,'registration/login.html',context)


def reg(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        

        
        else:
            messages.success(request,'User already have. Please sign in')
        

    context = {'form':form}

    return render(request,'registration/register.html',context) 
    

def profileview(request,id):


    return render(request,'main/profile.html',)
