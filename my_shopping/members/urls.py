from django.urls import path
from .import views

urlpatterns =[
    path('', views.members, name='members'),
    path('about', views.members1, name='home-v2.html'),  # Asosiy sahifa

]