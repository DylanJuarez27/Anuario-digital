from django.db import models
from Publicacion.models import Publicacion
from Perfil.models import Perfil

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    remitente = models.ForeignKey(Perfil, on_delete=models.CASCADE,null=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.publicacion}"