from django.db import models
from django.utils import timezone

class Institucion(models.Model):
    nombre_institucion = models.CharField(max_length=80)
    correo_institucion = models.EmailField()
    telefono_institucion = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_institucion

class Inscrito(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten')
    ]

    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    nro_personas = models.IntegerField(default=1)
    fecha_inscripcion = models.DateField(default=timezone.now)
    hora_inscripcion = models.TimeField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)
    institucion_asociada = models.ForeignKey('Institucion', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
