from django.contrib import admin
from django.db import models
from django.utils import timezone

class Solicitante(models.Model):
    SEXO = (
        ('02', 'Femenino'),
        ('01', 'Masculino'),
        ('00', 'No binario')
    )
    nombres = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    sexo = models.CharField(max_length=2, choices=SEXO, default=None)
    tipoDeDocumento = models.CharField(max_length=20, default=None)
    dni = models.CharField(max_length=8, default=None)
    cuil = models.CharField(max_length=13, default=None)
    email = models.CharField(max_length=20, default=None)
    genero = models.CharField(max_length=20, default=None)
    fechaNacimiento = models.DateField(default=None)
    nacionalidad = models.CharField(max_length=20, default=None)
    estadoCivil = models.CharField(max_length=20, null=True, default=None)

    def __str__(self):
        return self.nombres

class Ocupacion(models.Model):
    OCUPACION = (
                ('1', 'Ama de casa'),
                ('2', 'Changarin'),
                ('3', 'Estudiante'),
                ('4', 'Inactivo'),
                ('5', 'Jubilado/Pensionado'),
                ('6', 'Patrón o empleador'),
                ('7', 'Servicio doméstico'),
                ('8', 'Trabajo voluntario'),
                ('9', 'Cuenta propia'),
                ('10', 'Cuidado doméstico sin remuneración'),
                ('11', 'Desocupado'),
                ('12', 'Economía popular/asociativo'),
                ('13', 'Empleado de un sector privado')
    )
    CONDICION = (
                ('1' , 'Formal'),
                ('2', 'Informal')
    )
    FRECUENCIA = (
                ('1', 'Permanente'),
                ('2', 'Esporádico'),
                ('3', 'Temporario')
    )
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    ocupacion = models.CharField(max_length=20, choices=OCUPACION, default=None)
    condicion_laboral = models.CharField(max_length=20, choices=CONDICION, default=None)
    frecuencia_laboral = models.CharField(max_length=20, choices=FRECUENCIA, default=None)
    ingreso = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.solicitante

class Salud(models.Model):
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    enfermedad_cronica =  models.CharField(max_length=2, default=None)
    def __str__(self):
        return self.solicitante
