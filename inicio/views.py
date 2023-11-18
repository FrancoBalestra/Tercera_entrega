from django.shortcuts import render, redirect
from inicio.models import Notebook, Celular, Tablet
from inicio.forms import CrearNotebookFormulario, CrearCelularFormulario, CrearTabletFormulario, BusquedaNotebookFormulario

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

#formulario busqueda_notebooks
def notebooks(request):
    
    formulario = BusquedaNotebookFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_notebooks = Notebook.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaNotebookFormulario() 
    return render(request, 'inicio/notebook.html', {'formulario': formulario, 'listado_de_notebooks': listado_de_notebooks})

#formulario crear_notebook
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

#formulario crear_celular
def crear_celular(request):
    
    if request.method == 'POST':
        formulario_de_celulares = CrearCelularFormulario(request.POST)
        if formulario_de_celulares.is_valid():
            info_limpia = formulario_de_celulares.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            año = info_limpia.get('año')
            modelo = info_limpia.get('modelo')
            
            celular = Celular(marca=marca.lower(), descripcion=descripcion, año=año, modelo=modelo)
            celular.save()
        
            return redirect('crear_celular')
        else:
            formulario_de_celulares = CrearCelularFormulario()
            return render(request, 'inicio/crear_celular.html', {'formulario_de_celulares': formulario_de_celulares})
        
    formulario_de_celulares = CrearCelularFormulario()
    return render(request, 'inicio/crear_celular.html', {'formulario_de_celulares': formulario_de_celulares})

#formulario crear_tablet  
def crear_tablet(request):
    
    if request.method == 'POST':
        formulario_de_tablets = CrearTabletFormulario(request.POST)
        if formulario_de_tablets.is_valid():
            info_limpia = formulario_de_tablets.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            año = info_limpia.get('año')
            modelo = info_limpia.get('modelo')
            
            tablet = Tablet(marca=marca.lower(), descripcion=descripcion, año=año, modelo=modelo)
            tablet.save()
        
            return redirect('crear_tablet')
        else:
            formulario_de_tablets = CrearTabletFormulario()
            return render(request, 'inicio/crear_tablet.html', {'formulario_de_tablets': formulario_de_tablets})
        
    formulario_de_tablets = CrearTabletFormulario()
    return render(request, 'inicio/crear_tablet.html', {'formulario_de_tablets': formulario_de_tablets})
    
    
    
    
    
    
    
    
    