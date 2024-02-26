from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

STATUS_CHOICES = (
    ("active", "Active"),
    ("deactive", "Deactive")
)

class CustomUser(AbstractUser):
    image = models.ImageField(default=None, blank=True, null=True,)
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='created_by_user')
    created_at = models.DateField(default=datetime.now)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    descripton = models.TextField(default=None, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateField(default=datetime.now)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(default=None)
    price = models.CharField(max_length=80)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateField(default=datetime.now)

class ProductOfUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.now)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user_transactions')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user_transactions')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.now)

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user_requests')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user_requests')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    descripton = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateField(default=datetime.now)
