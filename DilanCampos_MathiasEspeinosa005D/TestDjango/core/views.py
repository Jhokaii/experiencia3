
from django.shortcuts import redirect, render
from django.views.decorators import csrf

from core.forms import PlantaForms
from .models import Categoria, Planta 

def index(request):
    return render (request, 'index.html')

def somos(request):
    return render (request, 'somos.html')

def contacto(request):
    return render (request, 'contacto.html')

def galeria(request):
    return render (request, 'galeria.html')

def registro(request):
    return render (request, 'registro.html')   




# Create your views here.
def mostrar(request):
    plantas = Planta.objects.all()

    datos = {
        'plantas' : plantas
    }
    return render(request, 'mostrar.html', datos)


def form_planta(request):
    if request.method=='POST':
        planta_form = PlantaForms(request.POST)
        if planta_form.is_valid():
            planta_form.save()
            return redirect('mostrar')
    else:
        planta_form = PlantaForms()
    return render(request, 'form_crear_planta.html', {'planta_form': planta_form})

def form_modplanta(request, id):
    planta = Planta.objects.get(nombre=id)
    datos ={
        'form': PlantaForms(instance = planta)
    }
    if request.method=='POST':
        planta_form = PlantaForms(request.POST)
        if planta_form.is_valid():
            planta_form.save()
            return redirect('mostrar')
    else:
        planta_form = PlantaForms()
    return render(request, 'form_modplanta.html', datos)

def form_de_planta(request, id):
    planta = Planta.objects.get(nombre=id)
    planta.delete()
    return redirect('mostrar')

