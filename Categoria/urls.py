from django.urls import path
from . import views

urlpatterns = [
    path('', views.Categoria_home, name='Categoria_home')
]