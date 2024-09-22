from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'modified_date', 'is_available')  # To'g'ri nomlar
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
