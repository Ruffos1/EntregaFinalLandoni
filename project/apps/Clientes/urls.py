from django.urls import path
from . import views

app_name = "Clientes"

urlpatterns = [
    path('', views.home, name="home"),
    path('crear/', views.crear_cliente, name="crear"),
    path('busqueda/', views.busqueda, name="busqueda"),
]