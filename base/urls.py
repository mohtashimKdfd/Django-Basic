#This file will render functions from base.views and route them to our main projects urls.py file
from django.urls import path
from . import views

urlpatterns =[
    #routes
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
] 