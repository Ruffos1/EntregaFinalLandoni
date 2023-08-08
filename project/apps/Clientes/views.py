from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import ClienteForm

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# Create your views here.
from .models import Cliente, Pais
# Create your views here.

def home(request):
    return render(request, "clientes/index.html")

def crear_cliente(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})


def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "dana"
    cliente_nombre = Cliente.objects.filter(nombre__contains="dana")

    # Nacimientos  mayores a 2000
    cliente_nacimiento = Cliente.objects.filter(
        nacimiento__gt=date(2000, 1, 1))

    # País de origen vacío
    cliente_pais = Cliente.objects.filter(pais_origen_id=None)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_nacimiento": cliente_nacimiento,
        "clientes_pais": cliente_pais
    }
    return render(request, "cliente/search.html", contexto)

from . import models
class ClienteList(ListView):
    model = models.Cliente

class ClienteDetail(DetailView):
    model = models.Cliente