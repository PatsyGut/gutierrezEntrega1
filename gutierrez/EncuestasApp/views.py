from django.shortcuts import render

# Create your views here.
from EncuestasApp.forms import ModalidadForm, CursoForm, EncuestaForm
from EncuestasApp.models import Modalidad, Curso, Encuesta


def inicio(request):
    return render(request, 'EncuestasApp/inicio.html')


def buscar(request):
    if request.GET.get("nombre", False):
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "EncuestasApp/resultadoBusqueda.html", {"cursos": cursos, "nombre": nombre})

    return render(request, 'EncuestasApp/buscar.html')


def modalidadForm(request):
    if request.method == "POST":
        formulario = ModalidadForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modalidad = Modalidad(
                nombre=informacion["nombre"],
                recursos_adicionales=informacion["recursos_adicionales"],
            )
            modalidad.save()
            return render(request, 'EncuestasApp/inicio.html')
    else:
        formulario = ModalidadForm()
    return render(request, 'EncuestasApp/ModalidadForm.html', {"formulario": formulario})


def cursoForm(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = Curso(
                codigo=informacion["codigo"],
                nombre=informacion["nombre"],
                cantidad_de_horas=informacion["cantidad_de_horas"],
                modalidad=informacion["modalidad"],
            )
            curso.save()
            return render(request, 'EncuestasApp/inicio.html')
    else:
        formulario = CursoForm()
    return render(request, 'EncuestasApp/CursoForm.html', {"formulario": formulario})


def encuestaForm(request):
    if request.method == "POST":
        formulario = EncuestaForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            encuesta = Encuesta(
                curso=informacion["curso"],
                valoracion=informacion["valoracion"],
                comentario=informacion["comentario"],
            )
            encuesta.save()
            return render(request, 'EncuestasApp/inicio.html')
    else:
        formulario = EncuestaForm()
    return render(request, 'EncuestasApp/EncuestaForm.html', {"formulario": formulario})
