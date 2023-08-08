from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    Proyecto = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Proyecto
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    proyecto_id = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

