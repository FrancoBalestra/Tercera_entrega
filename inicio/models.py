from django.db import models

class Notebook(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    año = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.año}'

class Celular(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField()
    año = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.año}'
    
class Tablet(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField()
    año = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.año}'

