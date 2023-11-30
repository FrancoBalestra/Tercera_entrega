from django import forms


class BaseNotebookFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    año = forms.IntegerField()

#CREACION DE FORMULARIOS
class CrearNotebookFormulario(BaseNotebookFormulario):
    ...

class CrearCelularFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    descripcion = forms.CharField()
    año = forms.IntegerField()

#BUSQUEDA DE FORMULARIO
class BusquedaNotebookFormulario(forms.Form): 
    marca = forms.CharField(max_length=30, required=False)   
    

#ACTUALIZACION DE FORMULARIO
class ActualizarNotebookFormulario(BaseNotebookFormulario):
    ...