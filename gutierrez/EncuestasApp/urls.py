from django.urls import path
from EncuestasApp import views

app_name = "EncuestasApp"
urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('buscar', views.buscar, name="Buscar"),
    path('ModalidadForm', views.modalidadForm, name="ModalidadForm"),
    path('CursoForm', views.cursoForm, name="CursoForm"),
    path('EncuestaForm', views.encuestaForm, name="EncuestaForm"),

]
