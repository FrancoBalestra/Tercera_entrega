from django import forms

class CrearNotebookFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    año = forms.IntegerField()
    
class BusquedaNotebookFormulario(forms.Form): 
    marca = forms.CharField(max_length=30, required=False)   
