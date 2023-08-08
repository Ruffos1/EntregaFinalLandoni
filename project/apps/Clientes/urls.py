from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

app_name = "Clientes"

urlpatterns = [
    path('', views.home, name="home"),
    path('crear/', views.crear_cliente, name="crear"),
    path('busqueda/', views.busqueda, name="busqueda"),
    path("MisClientes/", views.ClienteList.as_view(template_name="clientes/clientes_list.html"), name="clientes_list"),
    path("Clientes_detail/<int:pk>", views.ClienteDetail.as_view(template_name="clientes/clientes_detail.html"),name="clientes_detail"),
]

urlpatterns += staticfiles_urlpatterns()