from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="index"),
    path('login', login_, name="login"),
    path('grupos', grupos, name="grupos"),
    path('administrador', administrador, name="administrador"),
    path('cliente', cliente, name="cliente"),
    path('acerca', acerca, name="acerca")
]