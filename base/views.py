#Routes
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')

def index(reques):
    return HttpResponse('This is index page')
