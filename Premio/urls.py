from django.urls import path
from . import views

urlpatterns = [
    path('create_prize/<int:id>', views.create_prize, name='create_prize')
]