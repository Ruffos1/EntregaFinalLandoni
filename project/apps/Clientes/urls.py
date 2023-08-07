from django.urls import path
from . import views

app_name = "Clientes"

urlpatterns = [
    path('', views.home, name="home"),
]