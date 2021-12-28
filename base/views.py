#Routes
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, objectss

flag=0
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

# def authenticate(request):
#     if request.method == "POST":
#         username = request.POST.get

def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        data = objectss(name=name,description=description)
        data.save()

    return render(request,'base/forms.html')

def authenticate(request):
    if request.method == "POST":
        username = request.POST.get('name')
        userpwd = request.POST.get('password')
        if User.objects.filter(name=username,password=userpwd).exists():
            s="Logged in Success"
            global flag 
            flag=1
            return render(request,'base/user.html',{'result':s})
        else:
            return render(request,'base/signup.html',{'result':'Sign up!'})

def newUser(request):
    if request.method == "POST":
        namee = request.POST.get('name')
        passwords = request.POST.get('password')
        # users = User.objects.all()
        if User.objects.filter(name=namee).exists():
            s='User already registered || Try Logging in.'
            return render(request,'base/signin.html',{'result':s})
        else:
            if passwords == request.POST.get('repassword'):

                data = User(name=namee,password=passwords)
                data.save()
                s='Sign up Done||New User created'
                return render(request,'base/user.html',{'result':s})
            else:
                return render(request,'base/signup.html')
    return render(request,'base/signup.html')

    


def login(request):
    context = {'titles':"login page"}
    return render(request,'base/signin.html',context)

def signup(request):
    return render(request,'base/signup.html',{'titles':'Signup'})

def userPage(request):
    global flag
    if flag==1:
        return render(request,'base/user.html',{'result':"User is Logged in"})
    else:
        return render(request,'base/signin.html')

