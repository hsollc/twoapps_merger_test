from django.urls import path, include
from . import views

app_name = 'InterfaceApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('login/', views.login, name='login'),
]