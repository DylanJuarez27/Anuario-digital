from django.urls import path
from . import views

urlpatterns = [
    path('create_votation/', views.create_votation, name='create_votation')
]