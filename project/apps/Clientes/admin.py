from django.contrib import admin


# Register your models here.
from .models import Cliente, Pais, Proyecto

admin.site.register(Cliente)
admin.site.register(Pais)
admin.site.register(Proyecto)
