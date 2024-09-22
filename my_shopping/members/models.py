from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='photo/category', blank=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name