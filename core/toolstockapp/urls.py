from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="index"),
    path('login', login, name="login"),
    path('grupos', grupos, name="grupos")
]