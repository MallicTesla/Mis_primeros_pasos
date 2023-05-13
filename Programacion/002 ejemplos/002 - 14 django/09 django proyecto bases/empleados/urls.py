from django.urls import path
from . import views

urlpatterns = [
    path ("crear/", views.crear, name = "crear"),
    path ("contenido/", views.contenido, name = "contenido"),
    path ("", views.inicio, name = "inicio"),
    path ("menu/", views.menu, name = "menu"),
    path ("pablo/", views.pablo, name = "pablo"),
    path ("franco/", views.franco, name = "franco"),
    path ("german/", views.german, name = "german"),
    path ("marcelo/", views.marcelo, name = "marcelo"),
    path ("jorge/", views.jorge, name = "jorge"),
    path ("ale/", views.ale, name = "ale"),
    path ("matias/", views.matias, name = "matias"),
]