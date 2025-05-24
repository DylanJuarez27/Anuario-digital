from django.urls import path
from . import views

urlpatterns = [
    path('content_comment/<str:id>', views.content_comment_user, name='content_comment_user')
]