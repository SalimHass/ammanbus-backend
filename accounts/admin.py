from lib2to3.pgen2.driver import Driver
from django.contrib import admin
from .models import User,Passenger,Driver

# Register your models here.
admin.site.register(User)
admin.site.register(Passenger)
admin.site.register(Driver)
