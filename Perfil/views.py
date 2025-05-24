from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import localtime
from Perfil.models import Perfil
from Publicacion.forms import publication_user 
from Premio.forms import create_prize_user
from Votacion.forms import create_votation_user
from .forms import Edit_data
from django.contrib.auth import logout
from Grupo.models import Grupo
from Publicacion.models import Publicacion
from Comentario.forms import comment_user 
from Comentario.models import Comentario
from Premio.models import Premio
from Votacion.models import Votacion
from Nominacion.models import Nominacion
from PremiosGanados.models import PremiosGanados
from Voto.models import Voto
from Votacion.utils import limpiar_elecciones


@login_required
def user_profile(request):
   hoy = localtime(timezone.now()).date()
   perfil = request.user.perfil
   grupo = request.user.perfil.grupo
   amigos = Perfil.objects.filter(grupo=grupo)
   premios = Premio.objects.filter(grupo=grupo)
   eleccciones = Votacion.objects.filter(premio__in=premios)
   nominaciones = Nominacion.objects.filter(premio__in=premios)
   votos = Voto.objects.filter(votacion__in = eleccciones)
   ya_votados = {} 
   votado = False
   for eleccion in eleccciones:
      eleccion.nominacion = nominaciones.filter(premio=eleccion.premio)
   for eleccion in eleccciones:
       for nominacion in eleccion.nominacion:     
           perfiles_nominados = list(nominacion.perfiles_nominados.all())
           for perfil_votado in perfiles_nominados:
               votos_perfil = votos.filter(perfil_votado=perfil_votado,votacion=eleccion)
               if votos_perfil.filter(perfil_emisor=perfil).exists():
                  votado = True      
               perfil_votado.votos = votos_perfil
           nominacion.perfiles_nominados_list = perfiles_nominados
       ya_votados[eleccion.id] = votado
   eleccciones = list(eleccciones) 
   eleccciones = limpiar_elecciones(eleccciones) 
   premios_ganados = PremiosGanados.objects.filter(perfil__in=amigos)
   for amigo in amigos:
       amigo.premio_ganado_hoy = premios_ganados.filter(perfil=amigo,fecha_ganado__date=hoy).first()
   premios_perfil_ganados = premios_ganados.filter(perfil=perfil)
   amigos_count = len(amigos) - 1
   form = publication_user()
   form_comment = comment_user() 
   form_data = Edit_data()
   form_create_prize = create_prize_user()
   form_create_votation = create_votation_user()
   publicaciones = Publicacion.objects.filter(perfil_destino=perfil)
   comentarios = Comentario.objects.filter(publicacion__in=publicaciones)
   comentarios_por_publicacion = {
      pub.id: comentarios.filter(publicacion=pub) for pub in publicaciones
   }
   for pub in publicaciones:
      pub.comentarios = comentarios_por_publicacion.get(pub.id,[])
   return render(request, 'Perfil/user_profile.html',
                 {'perfil':perfil, 
                  'amigos':amigos, 
                  'publicaciones':publicaciones,
                  'elecciones': eleccciones, 
                  'amigos_count':amigos_count , 
                  'form':form, 
                  'form_comment':form_comment, 
                  'form_data':form_data ,
                  'form_create_prize': form_create_prize,
                  'form_create_votation': form_create_votation,
                  'ya_votados':ya_votados,
                  'premios_perfil_ganados':premios_perfil_ganados
                  })

@login_required
def users_profile(request,id):
   if request.user.id == id:
      return user_profile(request)
   else:
      hoy = localtime(timezone.now()).date()
      user = User.objects.get(id=id)
      perfil = user.perfil
      grupo = perfil.grupo
      amigos = Perfil.objects.filter(grupo=grupo)
      premios = Premio.objects.filter(grupo=grupo)
      eleccciones = Votacion.objects.filter(premio__in=premios)
      nominaciones = Nominacion.objects.filter(premio__in=premios)
      votos = Voto.objects.filter(votacion__in = eleccciones)
      premios_ganados = PremiosGanados.objects.filter(perfil__in=amigos)
      for amigo in amigos:
         amigo.premio_ganado_hoy = premios_ganados.filter(perfil=amigo,fecha_ganado__date=hoy).first()
      premios_perfil_ganados = PremiosGanados.objects.filter(perfil=perfil)    
      amigos_count = len(amigos) - 1
      form = publication_user()
      form_comment = comment_user()
      form_create_prize = create_prize_user()
      form_create_votation = create_votation_user()
      publicaciones = Publicacion.objects.filter(perfil_destino=perfil)
      comentarios = Comentario.objects.filter(publicacion__in=publicaciones)
      comentarios_por_publicacion = {
      pub.id: comentarios.filter(publicacion=pub) for pub in publicaciones
      }   
      for pub in publicaciones:
         pub.comentarios = comentarios_por_publicacion.get(pub.id,[])      
      return render(request, 'Perfil/user_profile.html', {
                     'perfil':perfil, 
                     'amigos':amigos,
                     'publicaciones':publicaciones,
                     'elecciones':eleccciones,
                     'amigos_count':amigos_count, 
                     'form':form, 
                     'form_comment':form_comment,
                     'form_create_prize': form_create_prize,
                     'form_create_votation': form_create_votation,
                     'premios_perfil_ganados':premios_perfil_ganados
                     })
   
@login_required
def edit_data_user(request):
    if request.method == 'POST':
       form = Edit_data(request.POST, request.FILES)
       if form.is_valid():
          descripcion = form.cleaned_data['descripcion']
          foto_portada = form.cleaned_data['foto_portada']
          foto_perfil = form.cleaned_data['foto_perfil']
          color_perfil = form.cleaned_data['color_perfil']
          fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
          perfil = request.user.perfil
          print(request.FILES)
          print("Portada:", foto_portada)
          print("Perfil:", foto_perfil)
          print("color:", color_perfil)
          print("fecha nacimiento:", fecha_nacimiento)           
          if descripcion:
             perfil.descripcion = descripcion
          if foto_portada:
             perfil.foto_portada = foto_portada
          if foto_perfil:
             perfil.foto_perfil = foto_perfil
          if color_perfil:   
             perfil.color_perfil = color_perfil
          if fecha_nacimiento:  
             perfil.fecha_nacimiento = fecha_nacimiento   
          perfil.save()    
    return redirect('user_profile')

@login_required
def cerrar_sesion(request):
   logout(request)
   return redirect('login')
      