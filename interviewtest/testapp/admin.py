from django.contrib import admin
from .models import Customer_details,Order,Product_details

# Register your models here.

# admin.site.register(Details) 

admin.site.register(Customer_details)
admin.site.register(Product_details)
admin.site.register(Order)