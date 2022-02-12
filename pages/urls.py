from django.urls import path
from pages import views

urlpatterns = [
    path('', views.pages, name='homePages'),
    path('newPost/', views.newPost, name='newPost')
]