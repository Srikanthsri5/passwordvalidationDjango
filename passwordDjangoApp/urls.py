from django.urls import path, include
from passwordDjangoApp import views
from . import views

app_name = 'passwordDjangoApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),

]