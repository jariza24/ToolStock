from dataclasses import fields
from django import forms
from .models import *

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': "form-control ",
        }
    ))

    precio = forms.FloatField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
        }
    ))

    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))

    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))

    """
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))
    """
    


    class Meta:

        model = Producto
        exclude = ['grupo'] 
        """['nombre','precio','unidad', 'proveedor','grupo']"""

class altProductoForm(forms.ModelForm):

    nombre = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': "form-control ",
        }
    ))

    precio = forms.FloatField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
        }
    ))

    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))

    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))

    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))

    """
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))
    """
    


    class Meta:

        model = Producto
        fields = ['nombre','precio','unidad', 'proveedor','grupo']
        """['nombre','precio','unidad', 'proveedor','grupo']"""

        

