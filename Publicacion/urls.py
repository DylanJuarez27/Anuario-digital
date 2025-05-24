from django.urls import path
from . import views

urlpatterns = [
    path('content_publication/<int:id>', views.content_publication, name='content_publication'),
    path('eliminate_publication/<int:id>', views.eliminate_publication, name='eliminate_publication')
]