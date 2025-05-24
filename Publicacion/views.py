from django.shortcuts import render,redirect,get_object_or_404
from .forms import publication_user 
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from Publicacion.models import Publicacion

def content_publication(request,id):
    if request.method == 'POST':
        form = publication_user(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data['descripcion']
            foto = form.cleaned_data['foto']
            user = User.objects.get(id=id)
            perfil = user.perfil
            Publicacion.objects.create(perfil_destino=perfil,perfil_origen=request.user.perfil,descripcion=descripcion,foto=foto)
    return redirect('users_profile', id=id)

@require_POST
def eliminate_publication(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)
    user = publicacion.perfil_destino.user
    publicacion.delete()
    return redirect('users_profile', id=user.id)

