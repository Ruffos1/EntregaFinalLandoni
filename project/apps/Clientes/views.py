from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path, reverse_lazy

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
            return redirect("Clientes:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "clientes/crear.html", {"form": form})




from . import models
class ClienteList(ListView):
    model = models.Cliente

class ClienteDetail(DetailView):
    model = models.Cliente

class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("Home:home")

from . import forms
class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("Home:home")