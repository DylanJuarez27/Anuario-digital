from django.urls import path
from . import views

urlpatterns = [
    path('', views.Grupo_home, name='Grupo_home')
]