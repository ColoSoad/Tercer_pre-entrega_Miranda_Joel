from django.urls import path, include
from .views import *
from .import views

urlpatterns = [
    # urls para los sitios de la pagina
    path('', index, name = 'inicio'),
    path('documentales/', documentales, name="documentales"),
    path('usuarios/', usuarios, name="usuarios"),
    path('peliculas/', peliculas, name="peliculas"),
    path('series/', series, name="series"),
   # urls para formularios de creacion ó agregar
    path('usuario_form/', usuarioForm, name="usuarioForm"),
    path('pelicula_form/', peliculaForm, name="peliculaForm"),
    path('serie_form/', serieForm, name="serieForm"),
    path('documental_form/', documentalForm, name="documentalForm"),
   # urls para formularios de búsqueda y resultado
    path('buscar_pelicula/', buscarPelicula, name="buscar_pelicula"),
    path('buscar2/', buscar2, name="buscar2"),

]