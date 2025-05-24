from django.db import models
from Perfil.models import Perfil
from Premio.models import Premio

class PremiosGanados(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    medalla = models.CharField(max_length=255)
    puntaje = models.PositiveIntegerField(null=True, blank=True)
    porcentaje_ganado = models.FloatField(null=True, blank=True)
    fecha_ganado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.perfil} ganó {self.premio} con {self.puntaje} votos ({self.porcentaje_ganado}%)"