from django.db import models

class Monitor(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)    
    fecha_de_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo}'