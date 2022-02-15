from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserEditForm

# Create your views here.

def inicioAccounts(req):
 return render(req, 'accounts/inicio.html') 

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login(request,user)
                return render(request, 'accounts/inicio.html', {'mensaje': f'Bienvenido {user.get_username()}'})
            else:
                return render(request, 'accounts/inicio.html', {'mensaje': 'Falló la autenticación'})
        else:
            return render(request, 'accounts/inicio.html', {'mensaje': 'Formulario erroneo'})
    
    else:
        form = AuthenticationForm()
        
        return render(request, 'accounts/login.html', {'form': form})

def singup_request(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'accounts/inicio.html', {'mensaje': 'Usuario Creado'})
        else:
            return render(request, 'accounts/inicio.html', {'mensaje': 'Usuario no creado'})
        
    else:
        form = UserCreationForm()
        return render(request, 'accounts/singup.html', {'form': form})



def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "homepage/index.html")
    else:
        miFormulario = UserEditForm(initial={ 'email':usuario.email})
        
        return render(request, "homepage/index.html", {"miFormulario":miFormulario, "ususario":usuario})


