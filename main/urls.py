from .views import *
from django.urls import path

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('support',SupportView.as_view(),name = 'support')
]
