from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

app_name = "Clientes"

urlpatterns = [
    path('', views.home, name="home"),
    path("MisClientes/", views.ClienteList.as_view(
        template_name="clientes/clientes_list.html"), name="clientes_list"),
    path("Clientes_detail/<int:pk>", views.ClienteDetail.as_view(
        template_name="clientes/clientes_detail.html"), name="clientes_detail"),
    path("Clientes_delete/<int:pk>", views.ClienteDelete.as_view(
        template_name="clientes/clientes_delete.html"), name="clientes_delete"),
    path("productocategoria/create/", views.ClienteCreate.as_view(
        template_name="clientes/crear.html"), name="clientes_create"),
]
urlpatterns += staticfiles_urlpatterns()