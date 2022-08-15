from datetime import date, datetime
from distutils.command import upload
from itertools import product
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

MANAGER='MANAGER'
CASHIER='CASHIER'

STATE_CHOICES = ( 
    ('Andhra Pradesh', 'Andhra Pradesh'), 
    ('Arunachal Pradesh', 'Arunachal Pradesh'), 
    ('Bihar', 'Bihar'), 
    ('Chhattisgarh', 'Chhattisgarh'), 
    ('Goa', 'Goa'), 
    ('Gujurat', 'Gujurat'), 
    ('Haryana', 'Haryana'), 
    ('Himachal Pradesh', 'Himachal Pradesh'), 
    ('Jharkhand', 'Jharkhand'), 
    ('Karnataka', 'Karnataka'), 
    ('Kerala', 'Kerala'), 
    ('Assam', 'Assam'), 
    ('Madhya Pradesh', 'Madhya Pradesh'), 
    ('Maharashtra', 'Maharashtra'), 
    ('Manipur', 'Manipur'), 
    ('Meghalaya', 'Meghalaya'), 
    ('Mizoram', 'Mizoram'), 
    ('Nagaland', 'Nagaland'), 
    ('Odisha', 'Odisha'), 
    ('Punjab', 'Punjab'), 
    ('Rajasthan', 'Rajasthan'), 
    ('Sikkim', 'Sikkim'), 
    ('Tamil Nadu', 'Tamil Nadu'), 
    ('Telangana', 'Telangana'), 
    ('Tripura', 'Tripura'), 
    ('Uttarakhand', 'Uttarakhand'), 
    ('Uttar Pradesh', 'Uttar Pradesh'), 
    ('West Bengal', 'West Benga'), 
)

STAFF_CATEGORY_CHOICES = (
    (MANAGER, 'Manager'),
    (CASHIER, 'Cashier')
)

CATEGORY_CHOICES = (
    ('Kitchen Steelproduct', 'Kitchen Steelproduct'), 
    ('Grocery', 'Grocery'), 
    ('Vegitables', 'Vegitables'), 
    ('Fresh Fruits', 'Fresh Fruits'), 
    ('Snacks', 'Snacks'), 
    ('Cold Drinks', 'Cold Drinks'), 
    ('Dryfruits & Nuts', 'Dryfruits & Nuts'), 
    ('Hot Drinks', 'Hot Drinks'), 
    ('Protins', 'Protins'), 
    ('Beauty Products', 'Beauty Products'),
    ('Other Home Products', 'Other Home Products'),
)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'), 
    ('Packed', 'Packed'), 
    ('On The Way', 'On The Way'), 
    ('Delivered', 'Delivered'), 
    ('Cancel', 'Cancel')
)

class User(AbstractUser):
    staff_category = models.CharField(choices=STAFF_CATEGORY_CHOICES, max_length=100)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    group = models.CharField(max_length=100)
    item_type = models.TextField()
    supplier = models.TextField()
    manufacturer = models.TextField()
    title = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)    
    item_size = models.CharField(max_length=100)
    item_color = models.CharField(max_length=100)    
    purchase_price = models.FloatField()
    purchase_tax = models.FloatField()
    selling_price = models.FloatField()
    selling_tax = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    actual_mrp = models.FloatField()
    product_purchase_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(auto_now_add=True)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

    class meta:
        db_table = "app_Product"  

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # title = models.ForeignKey(Product, on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to='productimage')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

