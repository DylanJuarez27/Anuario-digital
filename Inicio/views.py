from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import login_date, register_date
from Perfil.models import Perfil
from Grupo.models import Grupo



def init(request):
    return render(request,'Inicio/inicio.html')

def login_user(request):
    if request.method == 'POST':
       form = login_date(request.POST)
       if form.is_valid():
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          codigo_acceso = form.cleaned_data['codigo_acceso']

          user = authenticate(request,username=username, password=password)

          if user:
             try:
                group = user.perfil.grupo
                if group.codigo_acceso == codigo_acceso:
                   login(request,user)
                   return redirect('user_profile')
                else:
                   form.add_error('codigo_acceso', 'Codigo no valido')
             except:
                form.add_error(None,'Perfil no asignado')
          else:
            form.add_error(None, 'Usuario o contraseña incorrecta')                
    else:
      form = login_date()      
    return render(request,'Inicio/login.html',{'form':form})

def register_user(request):
    if request.method == 'POST':
       form = register_date(request.POST)
       if form.is_valid():
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          codigo_acceso = form.cleaned_data['codigo_acceso']

          try:
            group = Grupo.objects.get(codigo_acceso=codigo_acceso)
          except Grupo.DoesNotExist:
             form.add_error('codigo_acceso', 'Codigo de grupo invalido')
             return render(request,'Inicio/register.html',{'form':form})
          
          if User.objects.filter(username=username).exists():
             form.add_error('username', 'Usuario ya existe')
             return render(request,'Inicio/register.html',{'form':form})
          
          user = User.objects.create_user(username=username,password=password)
          perfil = Perfil.objects.create(user=user,grupo=group,descripcion='Nuevo Usuario')
          return redirect('login')
    else:
       form = register_date()    
    return render(request,'Inicio/register.html',{'form':form})