
from django.contrib import admin
from django.urls import path, include


from members.views import homev2
from django.conf.urls.static import static
from my_shopping.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homev2, name = "main"),
    path("", include("members.urls"))
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)


# urlpatterns  +=static