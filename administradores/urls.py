# mi_aplicacion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_view, name='formulario'),
    path('formulario2/', views.formulario2_view, name='formulario2'),
    path('notificacion/', views.notificacion_view, name='notificacion'),
    path('login/', views.login, name='login'),
    path('notificacion2/', views.notificacion2_view, name='notificacion2'),
    path('inicio/', views.inicio, name='inicio')
    ]
