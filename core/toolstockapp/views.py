from audioop import add, reverse
from logging import CRITICAL
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *
from .forms import *
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

    productos = Producto.objects.filter(id=id)

    return render(request, 'CRUD/ver_producto.html', {'productos':productos})

@login_required(login_url='/login')
def agregarProducto(request, id):
    
    data = {'form': ProductoForm()}
    if(request.method == 'POST'):
        formulario = ProductoForm(data=request.POST)
        if( formulario.is_valid() ):
            producto = formulario.save(commit=False)
            grupo = Grupo.objects.get(id=id)
            producto.grupo = grupo
            producto.save()
            messages.add_message(request, messages.SUCCESS, 'Producto agregado correctamente')
            return redirect(f'/administrador/{producto.grupo_id}')
        else:
            data['mensaje'] = 'Hubo un error'

    return render(request, 'CRUD/agregar_producto.html', data)

def agregarProductoAll(request):
    
    data = {'form': altProductoForm()}
    if(request.method == 'POST'):
        formulario = altProductoForm(data=request.POST)
        if( formulario.is_valid() ):
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Producto agregado correctamente')
            return redirect('/administrador/')
        else:
            data['mensaje'] = 'Hubo un error'

    return render(request, 'CRUD/agregar_producto.html', data)

def editarProducto(request, id):

    producto = Producto.objects.get(id=id)
    data = {'form': ProductoForm(instance=producto)}

    if ( request.method == 'POST' ):

        formulario = ProductoForm(data=request.POST, instance=producto)

        if (formulario.is_valid()):
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Producto editado correctamente')
            return redirect(f'/administrador/{producto.grupo_id}')
        else:
            data['mensaje'] = 'Hubo un error'
        
    return render(request, 'CRUD/editar_producto.html', data)

def eliminarProducto(request, id):

    producto = Producto.objects.get(id=id)
    producto.delete()
    
    if(producto.grupo_id > 6):
        messages.add_message(request, messages.SUCCESS, 'Producto eliminado correctamente')
        return redirect(f'/administrador/')
    else:
       messages.add_message(request, messages.SUCCESS, 'Producto eliminado correctamente')
       return redirect(f'/administrador/{producto.grupo_id}')


def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nombreProducto = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            unidad = form.cleaned_data['unidad']
            proveedor = form.cleaned_data['proveedor']

            producto = Producto.objects.create(
                nombre = nombreProducto,
                precio = precio,
                unidad = unidad,
                proveedor = proveedor
            )

def acerca(request):
    return render(request,'home/about.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
    
