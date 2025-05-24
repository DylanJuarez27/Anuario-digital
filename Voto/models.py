from django.db import models
from django.contrib.auth.models import User
from Perfil.models import Perfil
from Votacion.models import Votacion

class Voto(models.Model):
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, null=True)
    perfil_emisor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='votos_emitidos',null=True)
    perfil_votado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='votos_recibidos',null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.perfil_emisor} votó por {self.perfil_votado} en {self.votacion}"