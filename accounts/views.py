from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

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
