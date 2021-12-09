from django.contrib import admin
from .models import Manufacturer, Stock, Order, Customer, Employee, Sale
# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Sale)