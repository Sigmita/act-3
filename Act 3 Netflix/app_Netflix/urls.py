# app_Netflix/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_netflix, name='inicio_netflix'),
    path('usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/actualizar/<int:id_usuario>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/actualizar/realizar/<int:id_usuario>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuarios/borrar/<int:id_usuario>/', views.borrar_usuario, name='borrar_usuario'),
]