from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from .forms import *

urlpatterns = [
    path('',index,name='index'),
    #path('datos_admin',datos_admin,name='datos_admin'),
    path('add_nombre',add_nombre,name='add_nombre'),
    path('DatosForm',DatosForm,name='DatosForm'),
    path('descargar',descargar,name='descargar'),
    path('conectar', conectar,name='conectar'),

    path('delete_nombre/<int:myid>/',delete_nombre,name='delete_nombre'),
    path('edit_nombre/<int:myid>/',edit_nombre,name='edit_nombre'),
    path('update_nombre/<int:myid>/',update_nombre,name='update_nombre'),

]
