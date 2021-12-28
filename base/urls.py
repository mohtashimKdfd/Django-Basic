#This file will render functions from base.views and route them to our main projects urls.py file
from django.urls import path
from . import views

urlpatterns =[
    #routes
    path('',views.home,name='home'),
    path('index/<str:pk>/',views.index,name='index'),
    path('form',views.forms,name='forms'),
    path('save',views.save,name='save'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('newUser',views.newUser,name='newUser'), #handles sign up things
    path('user',views.userPage,name='user'),
    path('authenticate',views.authenticate,name='authenticate') #login auth
] 