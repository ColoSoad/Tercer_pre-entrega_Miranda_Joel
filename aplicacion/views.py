from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *

# Creacion de views para resolver urls:

# FUNCION PARA RENDERIZAR LA PAGINA DE INICIO
def index(request):
    return render(request, 'aplicacion/base.html')

# FUNCION PARA EL SITIO DE "DOCUMENTALES"
def documentales(request):
    contexto = {"documental": Documental.objects.all() }            
    return render(request, "aplicacion/documental.html", contexto)

# FUNCION PARA EL SITIO DE "USUARIOS"
def usuarios(request):
    contexto = {"usuario": Usuario.objects.all() }                  
    return render(request, "aplicacion/usuario.html", contexto)

# FUNCION PARA EL SITIO DE "SERIES"
def series(request):
    contexto = {"serie": Serie.objects.all() }                      
    return render(request, "aplicacion/serie.html", contexto)

# FUNCION PARA EL SITIO DE "PELICULAS"
def peliculas(request):
    contexto = {"pelicula": Pelicula.objects.all() }
    return render(request, "aplicacion/pelicula.html", contexto)

# FUNCION PARA CREAR NUEVOS "USUARIOS"
def usuarioForm(request):
    if request.method == "POST":   
        miForm = UsuarioForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get('nombre')
            usuario_apellido = miForm.cleaned_data.get('apellido')
            usuario = Usuario(nombre=usuario_nombre, apellido=usuario_apellido)
            usuario.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = UsuarioForm()

    return render(request, "aplicacion/usuarioForm.html", {"form":miForm})

# FUNCION PARA CREAR NUEVAS "PELICULAS"
def peliculaForm(request):
    if request.method == "POST":   
        miForm = PeliculaForm(request.POST)
        if miForm.is_valid():
            pelicula_nombre = miForm.cleaned_data.get('nombre')
            pelicula_año = miForm.cleaned_data.get('año')
            pelicula_genero = miForm.cleaned_data.get('genero')
            pelicula_plataforma = miForm.cleaned_data.get('plataforma')
            pelicula = Pelicula(nombre=pelicula_nombre, año=pelicula_año, genero=pelicula_genero, plataforma=pelicula_plataforma)
            pelicula.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PeliculaForm()

    return render(request, "aplicacion/peliculaForm.html", {"form":miForm})

# FUNCION PARA CREAR NUEVAS "SERIES"
def serieForm(request):
    if request.method == "POST":   
        miForm = SerieForm(request.POST)
        if miForm.is_valid():
            serie_nombre = miForm.cleaned_data.get('nombre')
            serie_año = miForm.cleaned_data.get('año')
            serie_genero = miForm.cleaned_data.get('genero')
            serie_plataforma = miForm.cleaned_data.get('plataforma')
            serie = Serie(nombre=serie_nombre, año=serie_año, genero=serie_genero, plataforma=serie_plataforma)
            serie.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = SerieForm()

    return render(request, "aplicacion/serieForm.html", {"form":miForm})

# FUNCION PARA CREAR NUEVOS "DOCUMENTALES"
def documentalForm(request):
    if request.method == "POST":   
        miForm = DocumentalForm(request.POST)
        if miForm.is_valid():
            documental_nombre = miForm.cleaned_data.get('nombre')
            documental_año = miForm.cleaned_data.get('año')
            documental_genero = miForm.cleaned_data.get('genero')
            documental_plataforma = miForm.cleaned_data.get('plataforma')
            documental = Documental(nombre=documental_nombre, año=documental_año, genero=documental_genero, plataforma=documental_plataforma)
            documental.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = DocumentalForm()

    return render(request, "aplicacion/documentalForm.html", {"form":miForm})

# FUNCION PARA BUSCAR CONTENIDO
def buscarPelicula(request):
    return render(request, "aplicacion/buscarPelicula.html")

# FUNCION PARA DEVOLVER EL RESULTADO DE LA BUSQUEDA DE "CONTENIDO"
def buscar2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        resultado_peliculas = Pelicula.objects.filter(nombre__icontains=nombre)
        resultado_documentales = Documental.objects.filter(nombre__icontains=nombre)
        resultado_series = Serie.objects.filter(nombre__icontains=nombre)
        if resultado_peliculas:
            return render(request, "aplicacion/resultadosPelicula.html", {"nombre": nombre, "resultados":resultado_peliculas})
        elif resultado_documentales:
            return render(request, "aplicacion/resultadosPelicula.html", {"nombre": nombre, "resultados": resultado_documentales})
        elif resultado_series:
            return render(request, "aplicacion/resultadosPelicula.html", {"nombre": nombre, "resultados": resultado_series})
        return render(request, "aplicacion/respuesta.html")
    else:
        return render(request, "aplicacion/base.html")