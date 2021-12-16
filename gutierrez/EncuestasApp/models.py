from django.db import models

# Create your models here.


class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)
    recursos_adicionales = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return f"{self.nombre}"


class Curso(models.Model):
    codigo = models.CharField(max_length=10, verbose_name='Código')
    nombre = models.CharField(max_length=100)
    cantidad_de_horas = models.IntegerField()
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"


class Encuesta(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    valoracion = models.IntegerField(verbose_name="Valoración")
    comentario = models.CharField(max_length=1000)

    def __str__(self):
        return f"({self.curso}) {self.valoracion}"
