from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from decimal import Decimal
from django.db.models import F, Sum

# Create your models here.
class Manufacturer(models.Model):
    manuf_ID = models.AutoField(primary_key=True)
    manuf_name = models.CharField(max_length=20)
    def __str__(self):
        return self.manuf_name

class Stock(models.Model):
    item_ID = models.AutoField(primary_key=True)
    manuf_ID = models.ForeignKey(Manufacturer, on_delete=CASCADE)
    item_name = models.CharField(max_length=20)
    item_model = models.CharField(max_length=20)
    item_quantity = models.IntegerField()
    item_cost = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.item_name

class Employee(models.Model):
    employee_ID = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    employee_pay = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.employee_name  + " " + self.l_name

class Order(models.Model):
    order_ID = models.AutoField(primary_key=True)
    item_ID = models.ForeignKey(Stock, on_delete=CASCADE)
    employee_ID = models.ForeignKey(Employee, on_delete=CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    order_cost = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.order_ID)
    

class Customer(models.Model):
    customer_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name + " " + self.l_name

class Sale(models.Model):
    sale_ID = models.AutoField(primary_key=True)
    customer_ID = models.ForeignKey(Customer, on_delete=CASCADE)
    item_ID = models.ForeignKey(Stock, on_delete=CASCADE)
    employee_ID = models.ForeignKey(Employee, on_delete=CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.sale_ID)

    #@property
    #def total_cost(self):
    #    return self.total_cost.aggregate(
    #        price=Sum(F('quantity') * F('item_ID__item_cost'))
    #    )['price'] or Decimal('0')
