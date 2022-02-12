from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Form para dar de alta un Post

class NewPost(forms.Form):
    #campos del formulario
    img = forms.ImageField()
    place = forms.CharField()
    name = forms.CharField()
    title = forms.CharField()
    description = forms.CharField()