from django.db import models
from Premio.models import Premio 
from Perfil.models import Perfil
from django.utils import timezone


class Nominacion(models.Model):
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    perfiles_nominados = models.ManyToManyField(Perfil)
    perfil_creador = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='nominaciones_creadas', null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Nominación para {self.premio.nombre} creada por {self.perfil_creador}"