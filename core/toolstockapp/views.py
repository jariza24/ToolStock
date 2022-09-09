from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def grupos(request):
    return render(request,'grupos/grupos.html')

def login_(request):
    if(request.method=='POST'):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if(user is not None):
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')

    else:
        return render(request, 'login/login.html')

def administrador(request):
    return render(request, 'administrador/admin.html')

def cliente(request):
    return render(request, 'cliente/cliente.html')

def acerca(request):
    return render(request,'home/about.html')
