from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("get/form/", views.getform, name = "form"),
    path ("get/destino/", views.getdestino, name = "destino"),
    path ("post/form/", views.postform, name = "postform"),
    path ("post/destino/", views.postdestino, name = "postdestino"),
]
