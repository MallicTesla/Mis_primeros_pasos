from catalogo import views
from django.urls import path

urlpatterns = [
    path (r"", views.index , name = "index")
]