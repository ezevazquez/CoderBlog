from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.pages, name='homePages'),
    path('newPost/', views.newPost, name='newPost'),
    path('postDetail/<pk>', views.PostDetail.as_view(), name = 'postDetail'),
    path('postDelete/<pk>', views.PostDelete.as_view(), name = 'postDelete'),
    
    path('postUpdate/<post_id>/',views.postUpdate, name = "postUpdate"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)