from django.db import models

# Create your models here.

class MenuItem(models.Model):
    category = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

class Customer(models.Model):
    address = models.CharField(max_length = 500)
    name = models.CharField(max_length = 100)

class Order(models.Model):
    address = models.CharField(max_length = 500)
    group = models.ManyToManyField(Customer)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    spice_level = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)