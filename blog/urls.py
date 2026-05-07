from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autor/', views.crear_autor, name='autor'),
    path('post/', views.crear_post, name='post'),
    path('comentario/', views.crear_comentario, name='comentario'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
