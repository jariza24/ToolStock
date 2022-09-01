from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def grupos(request):
    return render(request,'grupos/grupos.html')

def login(request):
    return render(request, 'login/login.html')
