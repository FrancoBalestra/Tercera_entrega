from django.db import models

class Celular(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField()
    año = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.año}'
