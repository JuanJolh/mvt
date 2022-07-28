from django.contrib import admin
from django.urls import path
from familia.views import plantilla, agregar_familia, lista_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantilla/', plantilla, name='plantilla'),
    path('agregar_familia/', agregar_familia, name='agregar_familia'),
    path('lista_familiares/', lista_familiares, name='lista_familiares')
]