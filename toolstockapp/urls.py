from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="index"),
    path('login', login_, name="login"),
    path('gruposcliente', gruposCliente, name="gruposcliente"),
    path('gruposadmin', gruposAdmin, name="gruposadmin"),
    path('administrador/<int:id>', administrador, name="administrador"),
    path('verproducto/<int:id>', verProducto, name="verproducto"),
    path('agregarproducto/<int:id>', agregarProducto, name="agregarproducto"),
    path('agregarproducto/', agregarProductoAll, name="agregarproductoall"),
    path('editarproducto/<int:id>', editarProducto, name="editarproducto"),
    path('eliminarproducto/<int:id>', eliminarProducto, name="eliminarproducto"),
    path('administrador/', administradorAll, name="administrador"),
    path('cliente/', clienteAll, name="cliente"),
    path('cliente/<int:id>', cliente, name="cliente"),
    path('acerca', acerca, name="acerca"),
    path('logout', logoutUser, name="logout"),
]