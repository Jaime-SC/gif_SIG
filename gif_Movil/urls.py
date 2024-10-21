# mi_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_gif, name='mostrar_gif'),
]
