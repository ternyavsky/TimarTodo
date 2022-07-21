from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('support',SupportView.as_view(),name = 'support'),
    path('examples',ExamplesView.as_view(), name = 'examples'),
    path('registration',RegistrationView.as_view(), name = 'register'),
    path('profile<int:user_id>',ProfileView.as_view(),name = 'profile')
    
]
