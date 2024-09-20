
from django.contrib import admin
from django.urls import path, include
from members.views import *
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("members.urls"))
]


# urlpatterns  +=static