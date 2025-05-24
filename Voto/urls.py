from django.urls import path
from . import views

urlpatterns = [
    path('votar/<int:id>', views.Votar, name='votar')
]