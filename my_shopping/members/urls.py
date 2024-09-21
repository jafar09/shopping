from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('views/', members),
    path('edit/', about),
    path('edit1/', contactv1),
    path('edit2/', contactv2),
    path('edit3/', faq),
    path('home2/', homev2),
    path('homefull3/', homev3fullcolorbg),
    path('home3/', homev3),
    path('home4/', homev4),
    path('home5/', homev5),
    path('home6/', homev6),
    path('home7/', homev7),
    path('index1/', storedirectory),
    path('index2/', termsandconditions),

    path("news/<int:id>",yangilik),

]