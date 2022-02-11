from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.inicioAccounts, name='inicioAccounts'),
    path("login/", views.login_request, name='Login'),
]