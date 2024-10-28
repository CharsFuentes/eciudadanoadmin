# mi_aplicacion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_view, name='formulario'),
    path('notificacion/', views.notificacion_view, name='notificacion'),
    path('login/', views.login, name='login')
]
