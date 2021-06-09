from django.db import models
from django.shortcuts import reverse

# Create your models here.
from django.contrib.auth.models import User


class UserModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    img = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Product(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=30)
#     price = models.IntegerField()
#     def __str__(self):
#         return self.titlepython
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    instrument_purchase = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    product_quantity = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_name')
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class TheProduct(models.Model):
    DEPTS = (
        ('Pastries', 'Pastries'),
        ('Beverages', 'Beverages'),
        ('Wine', 'Wine'),
        ('Detergents', 'Detergents'),
    )

    name = models.CharField('Name', max_length=20, unique=True)
    category = models.CharField(verbose_name='Select Category', max_length=20, choices=DEPTS)
    image = models.ImageField(upload_to='product_image')
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
