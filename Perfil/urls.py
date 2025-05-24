from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/',views.user_profile,name='user_profile'),
    path('user_profile/<int:id>', views.users_profile,name='users_profile'),
    path('edit_data_user/', views.edit_data_user,name='edit_data_user'),
    path('cerrar_sesion/', views.cerrar_sesion,name="cerrar_sesion")
]