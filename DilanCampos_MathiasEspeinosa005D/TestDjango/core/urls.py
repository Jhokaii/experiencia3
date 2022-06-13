from django.urls import path 
from .views import index, contacto, galeria, registro, somos, form_planta, form_modplanta, form_de_planta, mostrar  



urlpatterns = [
    path('', index, name = "index"),
    path('contacto/', contacto,  name = "contacto" ),
    path('galeria/', galeria, name = "galeria" ),
    path('registro/', registro, name = "registro"),
    path('somos/', somos, name = "somos"),
    path('mostrar/', mostrar, name= "mostrar"),
    path('form_planta/<id>', form_planta, name = "form_planta"),
    path('form_modplanta/<id>', form_modplanta, name= "form_modplanta"),
    path('form_de_planta/<id>>', form_de_planta, name= "form_de_planta")

]