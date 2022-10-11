from django.urls import path, include
from . import views

app_name = 'InterfaceApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('performance/', views.performance, name='performance'),
    path('signup/', views.signup, name='signup'),
]