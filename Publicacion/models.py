from django.db import models
from Perfil.models import Perfil

class Publicacion(models.Model):
    perfil_destino = models.ForeignKey(Perfil, on_delete=models.CASCADE,related_name='publicaciones_recibidas' )
    perfil_origen = models.ForeignKey(Perfil,on_delete=models.SET_NULL,null=True,blank=True,related_name='publicaciones_enviadas')
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='fotos_publicacion/',blank=True,null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Publicación de {self.perfil_destino}"