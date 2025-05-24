from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=255)
    codigo_acceso = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
