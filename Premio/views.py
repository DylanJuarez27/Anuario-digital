from django.shortcuts import render, redirect
from .forms import create_prize_user
from Premio.models import Premio
from django.contrib.auth.models import User

def create_prize(request,id):
    if request.method == 'POST':
        form =  create_prize_user(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            categoria = form.cleaned_data['categoria']
            user = User.objects.get(id=id)
            perfil = user.perfil
            grupo = perfil.grupo
            Premio.objects.create(nombre=nombre,descripcion=descripcion,categoria=categoria,grupo=grupo)
    return redirect(f'/Perfil/user_profile/{id}#agregarPremio')