from django.urls import path
from pages import views

urlpatterns = [
    path('', views.pages, name='homePages'),
    path('newPost/', views.newPost, name='newPost'),
    path('postDetail/<pk>', views.PostDetail.as_view(), name = 'postDetail'),
    path('postDelete/<pk>', views.PostDelete.as_view(), name = 'postDelete'),
    path('postUpdate/<pk>', views.PostUpdate.as_view(), name = 'postUpdate'),
    
]