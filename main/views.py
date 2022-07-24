from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView

from main.models import Task
from .forms import LoginForm, RegistrationForm, TaskForm
# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'

class SupportView(TemplateView):
    template_name = 'main/support.html'

class ExamplesView(TemplateView):
    template_name = 'main/examples.html'

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
    object = Task.objects.get(id=id)
    object.delete()
    return redirect('tasklist') 

def deleteall(request):
    objects = Task.objects.filter(author_id = request.user)
    objects.delete()
    return redirect('tasklist')



   




    
    

        
      


class TaskListView(ListView):
    template_name = 'examples/tasklist.html'
    model = Task

  
        

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


