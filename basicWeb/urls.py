from django.contrib import admin
from django.urls import path ,include

# def home(request):
#     return HttpResponse('Home page')  [~This all is stored in urls.py of our app (in our case it is base that we created using python3 manage.py startapp base )]

# def index(reques):
#     return HttpResponse('This is index page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
]