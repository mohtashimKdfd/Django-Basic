#Routes
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

objects = ['people','animals','world','aliens']


def home(request):
    context = {'obj':objects}
    return render(request,'base/home.html',context)

def index(request):
    return render(request,'base/index.html')
