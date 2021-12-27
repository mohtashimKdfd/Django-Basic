#Routes
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

objects = [
    {'id':1,'name':'people'},
    {'id':2,'name':'animals'},
    {'id':3,'name':'world'},
    {'id':4,'name':'aliens'},
    ]


def home(request):
    context = {'obj':objects}
    return render(request,'base/home.html',context)

def index(request,pk):
    context = {'obj':objects[int(pk)]}
    return render(request,'base/index.html',context)
