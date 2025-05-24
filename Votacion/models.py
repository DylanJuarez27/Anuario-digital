from django.db import models
from Premio.models import Premio
from django.utils import timezone

class Votacion(models.Model):
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f"Votación para {self.premio.nombre}"
