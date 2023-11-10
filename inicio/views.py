from django.shortcuts import render, redirect
from inicio.models import Notebook
from inicio.forms import CrearNotebookFormulario, BusquedaNotebookFormulario

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def notebooks(request):
    
   # marca_a_buscar = request.GET.get('marca')
    
   # if marca_a_buscar:
   #     listado_de_notebooks = Notebook.objects.filter(marca__icontains=marca_a_buscar)
   # else:
   #     listado_de_notebooks = Notebook.objects.all()
    
    
    formulario = BusquedaNotebookFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_notebooks = Notebook.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaNotebookFormulario() 
    return render(request, 'inicio/notebook.html', {'formulario': formulario, 'listado_de_notebooks': listado_de_notebooks})

def crear_notebook(request):
    
    if request.method == 'POST':
        formulario = CrearNotebookFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            año = info_limpia.get('año')
            
            notebook = Notebook(marca=marca.lower(), descripcion=descripcion, año=año)
            notebook.save()
        
            return redirect('notebooks')
        else:
            return render(request, 'inicio/crear_notebook.html', {'formulario': formulario})
        
    formulario = CrearNotebookFormulario()
    return render(request, 'inicio/crear_notebook.html', {'formulario': formulario})