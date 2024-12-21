from django.db import models

class Institucion(models.Model):
    nombre_institucion = models.CharField(max_length=255)
    correo_institucion = models.EmailField()
    telefono_institucion = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_institucion

class Inscrito(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    institucion_asociada = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
