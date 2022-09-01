from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login', login),
    path('grupos', grupos)
]