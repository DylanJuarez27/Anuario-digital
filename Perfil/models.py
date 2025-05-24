from django.db import models
from django.contrib.auth.models import User
from Grupo.models import Grupo


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    foto_perfil = models.ImageField(upload_to='fotos_perfil/',blank=True,null=True)
    foto_portada = models.ImageField(upload_to='fotos_portada/',blank=True,null=True)
    color_perfil = models.CharField(max_length=20,default='#f0f2f5')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    unique_user_perfil = models.UniqueConstraint(fields=['grupo'], name='unique_grupo_id')

    def __str__(self):
        return f"{self.user.username}"