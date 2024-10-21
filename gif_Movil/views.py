# mi_app/views.py

from django.shortcuts import render

def mostrar_gif(request):
    return render(request, 'mostrar_gif.html')
