"""miproyrcto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# tambien se puede hacer asi
# from django.urls import include
#   despues ay que importar esto
from django.conf import settings
from django.conf.urls.static import static

# esto es para controlar los patrones de la url 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'))
#   esto se agrega despues de crear el archivo html
] + static (settings.STATIC_URL, document_root = settings.STATIC_URL)