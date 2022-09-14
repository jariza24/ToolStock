from audioop import reverse
from logging import CRITICAL
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def gruposCliente(request):
    grupos={
        'id1':1,
        'id2':2,
        'id3':3,
        'id4':4,
        'id5':5,
        'id6':6
    }
    return render(request,'grupos/gruposCli.html', {'id':grupos})

@login_required(login_url='/login')
def gruposAdmin(request):
    grupos={
        'id1':1,
        'id2':2,
        'id3':3,
        'id4':4,
        'id5':5,
        'id6':6
    }
    return render(request,'grupos/gruposAdm.html', {'id':grupos})

def login_(request):
    if(request.method=='POST'):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if(user is not None):
            login(request, user)
            return redirect('/gruposadmin')
        else:
            messages.add_message(request, messages.ERROR, 'Las credenciales no son correctas')
            return redirect('/login')

    else:
        return render(request, 'login/login.html')

@login_required(login_url='/login')
def administrador(request, id):
    if(id > 6):
        grupos = [{'nombre':'Todos los Productos'}]
        productos = Producto.objects.all()
        return render(request, 'administrador/admin.html', {'productos':productos, 'grupos':grupos})
    else:
        grupos = Grupo.objects.filter(id=id)
        productos = Producto.objects.filter(grupo_id=id)
        return render(request, 'administrador/admin.html', {'productos':productos, 'grupos':grupos})

@login_required(login_url='/login')
def administradorAll(request):
    grupos = [{'nombre':'Todos los Productos'}]
    productos = Producto.objects.all()

    return render(request, 'administrador/admin.html', {'productos':productos, 'grupos':grupos})

def cliente(request, id):
    if(id > 6):
        grupos = [{'nombre':'Todos los Productos'}]
        productos = Producto.objects.all()
        return render(request, 'cliente/cliente.html', {'productos':productos, 'grupos':grupos})
    else:
        grupos = Grupo.objects.filter(id=id)
        productos = Producto.objects.filter(grupo_id=id)
        return render(request, 'cliente/cliente.html', {'productos':productos, 'grupos':grupos})

def clienteAll(request):
    grupos = [{'nombre':'Todos los Productos'}]
    productos = Producto.objects.all()

    return render(request, 'cliente/cliente.html', {'productos':productos, 'grupos':grupos})

def verProducto(request, id):

    productos = Producto.objects.filter(grupo_id=id)

    return render(request, 'CRUD/crear_producto.html', {'productos':productos})

def acerca(request):
    return render(request,'home/about.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
    
