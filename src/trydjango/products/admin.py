from django.contrib import admin

# Register your models here.
from .models import Product
#Imports Product class from the current directory
#relative import of class works
admin.site.register(Product)
