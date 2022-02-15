from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Form para dar de alta un Post

class NewPost(forms.Form):
    #campos del formulario
    place = forms.CharField(label='Nombre del Lugar')
    name = forms.CharField(label='Nombre')
    title = forms.CharField(label='Titulo')
    description = forms.CharField(label='Contanos de tu viaje y comparti tu experiencia')
    img = forms.FileField(label= 'Imagenes', required=False)