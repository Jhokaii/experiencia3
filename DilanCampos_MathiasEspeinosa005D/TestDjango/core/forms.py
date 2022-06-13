from cProfile import label
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Planta



class   PlantaForms(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'color']
        labels ={
            'nombre' : 'Nombre',
            'color' : 'Color',
    
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese nombre de la planta',
                'id' : 'nombre'
                }
            ),

            'color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el color de la planta',
                    'id' : 'color'
                }
            )

        }
