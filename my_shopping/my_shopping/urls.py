
from django.contrib import admin
from django.urls import path, include
from members.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("members.urls"))
]
