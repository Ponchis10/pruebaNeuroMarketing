from django.shortcuts import render

# Create your views here.

def home_usuario(request):
    return render(request, 'usuario/home_usuario.html')

def editar_usuario(request):
    return render(request, 'usuario/editar_usuario.html')