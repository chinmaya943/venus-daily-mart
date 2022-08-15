from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    User,
    Image,

)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'staff_category']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Staff Category"), {"fields": ("staff_category",)}),
    )

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','group','item_type', 'supplier', 'manufacturer', 'title', 'barcode', 'item_size', 'item_color', 'purchase_price', 'purchase_tax', 'selling_price', 'selling_tax', 'discounted_price', 'description', 'brand', 'category', 'actual_mrp', 'product_purchase_date', 'expiry_date', 'product_image']

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'pimage']

@admin.register(Cart)
class CartModelAdmin9(admin.ModelAdmin):
    list_display = ['id' ,'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'order_date', 'status']

