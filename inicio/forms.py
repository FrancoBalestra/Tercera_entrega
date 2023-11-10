from django import forms

#CREACION DE FORMULARIOS
class CrearNotebookFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    año = forms.IntegerField()

class CrearCelularFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    descripcion = forms.CharField()
    año = forms.IntegerField()

class CrearTabletFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    descripcion = forms.CharField()
    año = forms.IntegerField()

def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.año}'


#BUSQUEDA DE FORMULARIO
class BusquedaNotebookFormulario(forms.Form): 
    marca = forms.CharField(max_length=30, required=False)   