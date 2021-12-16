from django import forms

from EncuestasApp.models import Modalidad, Curso


class ModalidadForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    recursos_adicionales = forms.BooleanField(required=False)


class CursoForm(forms.Form):
    codigo = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=100)
    cantidad_de_horas = forms.IntegerField()
    modalidad = forms.ModelChoiceField(queryset=Modalidad.objects.all())


class EncuestaForm(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
    valoracion = forms.IntegerField()
    comentario = forms.CharField(max_length=1000)
