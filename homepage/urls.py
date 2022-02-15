from django.urls import path
from homepage import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("aboutus", views.aboutus, name='aboutus'),
]