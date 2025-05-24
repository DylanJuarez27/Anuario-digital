from django.shortcuts import render, redirect
from Votacion.forms import create_votation_user
from django.contrib.auth.decorators import login_required
from .models import Nominacion
from django.contrib.auth.models import User
from Votacion.models import Votacion



@login_required
def create_nomination_user(request):
    if request.method == 'POST':
        form = create_votation_user(request.POST)
        if form.is_valid():
            premio = form.cleaned_data['premio']
            if Votacion.objects.filter(premio=premio):
                form.add_error('premio','Premio ya en votacion')
                return redirect(f'/Perfil/user_profile/#votaciones-agregarPremio')
            perfiles_nominados = form.cleaned_data['perfiles_nominados']
            fecha_fin = form.cleaned_data['fecha_fin']
            user = request.user
            perfil_creador = user.perfil
            nominacion = Nominacion.objects.create(premio=premio)
            nominacion.perfiles_nominados.set(perfiles_nominados)
            nominacion.perfil_creador = perfil_creador 
            nominacion.save()
            Votacion.objects.create(premio=premio,fecha_fin=fecha_fin)
    return redirect(f'/Perfil/user_profile/#votaciones')