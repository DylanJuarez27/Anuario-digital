from django.urls import path
from . import views

urlpatterns = [
    path('create_nomination/', views.create_nomination_user, name='create_nomination')
]