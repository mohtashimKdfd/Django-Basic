from django.contrib import admin

# Register your models here.

from .models import objectss, User


admin.site.register(objectss)
admin.site.register(User)