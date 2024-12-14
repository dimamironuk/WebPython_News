from django.contrib import admin
from django.urls import path
from posts.views import post_list, create_post  
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),  
    path('posts/create/', create_post, name='create_post'),  
]
