from django.contrib import admin 
from .models import category 


class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(category, categoryAdmin)