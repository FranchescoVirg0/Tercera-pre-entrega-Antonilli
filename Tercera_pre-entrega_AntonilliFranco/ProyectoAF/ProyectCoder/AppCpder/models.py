from django.db import models

# Create your models here.

class Consorcista(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    Unidad_Funcional = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Administrador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
       return f'{self.nombre} - {self.apellido}'

class Expensa(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_venc = models.DateField()
    pagada = models.BooleanField()
    
    def __str__(self):
        return f'{self.nombre}'
    