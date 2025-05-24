from django.shortcuts import render,redirect
from Votacion.models import Votacion
from Voto.models import Voto
from Perfil.models import Perfil

def Votar(request, id):      
    if request.method == 'POST':
        perfil_id = request.POST.get('perfil_id')
        eleccion = Votacion.objects.get(id=id)
        perfil_votado = Perfil.objects.get(id=perfil_id)
        perfil_emisor = request.user.perfil
        Voto.objects.create(votacion=eleccion,perfil_emisor=perfil_emisor,perfil_votado=perfil_votado)
    return redirect(f'/Perfil/user_profile/{perfil_emisor.user.id}#votaciones-modalVotacion{id}')