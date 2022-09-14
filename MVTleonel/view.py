from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def papa(request, padre):
    nombre: "Norberto"
    edad: 56
    fecha: datetime.now().year - edad
    resultado = f"Mi padre se llama {nombre},su edad es {edad}, y su fecha de nacimiento es {fecha}"
    return HttpResponse(resultado)


def mama(request, madre):
    nombre: "Patricia"
    edad: 52
    fecha: datetime.now().year - edad
    resultado = f"Mi madre se llama {nombre},su edad es {edad}, y su fecha de nacimiento es {fecha}"
    return HttpResponse(resultado)


def brother(request, hermano):
    nombre: "Julian"
    edad: 29
    fecha: datetime.now().year - edad
    resultado = f"Mi hermano se llama {nombre},su edad es {edad}, y su fecha de nacimiento es {fecha}"
    return HttpResponse(resultado)


def template_1(request):
    return render(request, 'template1.html')
