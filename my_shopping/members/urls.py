from django.urls import path
from .import views

urlpatterns =[
    path('members/', views.members, name='members'),
    path('', views.home, name='home-v3.html'),  # Asosiy sahifa

]