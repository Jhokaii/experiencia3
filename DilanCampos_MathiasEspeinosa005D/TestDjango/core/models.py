from pyexpat import model
from django.db import models
from cgi import print_arguments

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    

    def __str__(self):
        return self.nombreCategoria

class Planta (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre')
    color = models.CharField(max_length=50, verbose_name='Color de la planta')

    

    def __str__(self):
        return self.nombre

 