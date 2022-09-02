from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_usuario, name='home_usuario'),
    path('editar_usuario', views.editar_usuario, name='editar_usuario'),
]