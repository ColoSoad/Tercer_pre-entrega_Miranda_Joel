from django import forms

# FORMULARIO PARA LA CREACION DE USUARIOS
class UsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre de Usuario", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido de Usuario", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)

# FORMULARIO PARA LA CREACION DE NUEVAS PELICULAS
class PeliculaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la película", max_length=50, required=True)
    año = forms.IntegerField(label= "Año de la película", required=False)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

# FORMULARIO PARA LA CREACION DE NUEVAS SERIES
class SerieForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la serie", max_length=50, required=True)
    año = forms.IntegerField(label= "Año de la serie", required=False)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

# FORMULARIO PARA LA CREACION DE NUEVOS DOCUMENTALES
class DocumentalForm(forms.Form):
    nombre = forms.CharField(label="Nombre del documental", max_length=50, required=True)
    año = forms.IntegerField(label= "Año del documental", required=False)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

# FORMULARIO PARA LA BUSQUEDA
class BusquedaMany(forms.Form):
    nombre = forms.CharField(label = "Buscar Contenido", max_length=30, required=True)
