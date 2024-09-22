from django.db import models
from members.models import category  # To'g'ri yozilishi kerak

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Mahsulot nomi
    slug = models.SlugField(max_length=100, unique=True)  # Slug
    description = models.TextField(max_length=500, blank=True)  # Mahsulot tavsifi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField to'g'rilandi
    image = models.ImageField(upload_to='photos/products')  # Fayl saqlash yo'li to'g'rilandi
    stock = models.IntegerField(default=100)  # Mahsulotning zaxiradagi miqdori
    is_available = models.BooleanField(default=True)  # Mavjudlik holati
    category = models.ForeignKey(category, on_delete=models.CASCADE)  # Category modelini to'g'ri import qildik
    created_date = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana
    modified_date = models.DateTimeField(auto_now=True)  # Tahrirlangan sana

    def __str__(self):
        return self.name
