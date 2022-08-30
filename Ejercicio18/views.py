from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse 

# Create your views here.

def familiar1(request):
    familiar1= Familiar(nombre="Gabriela",apellido="Ojeda",parentesco="hermana",email="email@etc")
    familiar1.save()
    texto= f"Nombre {familiar1.nombre} Apellido {familiar1.apellido} Parentesco {familiar1.parentesco} Email {familiar1.email}"
    return HttpResponse(texto)

def familiar2(request):
    familiar2 = Familiar(nombre="Leonardo",apellido="Ojeda",parentesco="hermano",email="email2@etc")
    familiar2.save()
    texto= f"Nombre {familiar2.nombre} Apellido {familiar2.apellido} Parentesco {familiar2.parentesco} Email {familiar2.email}"
    return HttpResponse(texto)

def familiar3(request):
    familiar3 = Familiar(nombre="Maria",apellido="Corsi",parentesco="abuela",email="404 not found lol")
    familiar3.save()
    texto= f"Nombre {familiar3.nombre} Apellido {familiar3.apellido} Parentesco {familiar3.parentesco} Email {familiar3.email}"
    return HttpResponse(texto)