from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("form/", views.form, name = "form"),
    path ("destino/", views.destino, name = "destino"),
]
