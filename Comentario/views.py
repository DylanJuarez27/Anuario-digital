from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import comment_user
from Comentario.models import Comentario
from Publicacion.models import Publicacion

def  content_comment_user(request,id):
    if request.method == 'POST':
        form = comment_user(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            publicacion = Publicacion.objects.get(id=id)
            Comentario.objects.create(publicacion=publicacion,remitente=request.user.perfil,contenido=contenido)
            perfil_destino = publicacion.perfil_destino
    return redirect(f'/Perfil/user_profile/{perfil_destino.user.id}#modal{id}-comentarios')