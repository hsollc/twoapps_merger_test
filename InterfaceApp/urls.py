from django.urls import  path, include
from . import views

app_name = 'InterfaceApp'

urlpatterns = [
    path('', views.index),
]