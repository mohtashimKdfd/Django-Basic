#Routes
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import objectss

# objects = [
#     {'id':1,'name':'people'},
#     {'id':2,'name':'animals'},
#     {'id':3,'name':'world'},
#     {'id':4,'name':'aliens'},
#     ]


def home(request):
    objectt = objectss.objects.all()
    context = {'obj':objectt}
    return render(request,'base/home.html',context)

def index(request,pk):
    objectt = objectss.objects.all()
    print(type(objectt))
    # context = {'obj':objectt[int(pk)-1]}
    # context = {'obj':objects[int(pk)-1]}
    x = objectss.objects.get(id=pk)
    print(x.name)
    context = {'obj':x}
    return render(request,'base/index.html',context)


def forms(request):
    context = {
        'titles ': 'Forms'
    }
    return render(request,'base/forms.html',context)

def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        data = objectss(name=name,description=description)
        data.save()

    return render(request,'base/forms.html')
