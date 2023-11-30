from django.shortcuts import render, redirect
from inicio.models import Notebook, Celular
from inicio.forms import CrearNotebookFormulario, CrearCelularFormulario, BusquedaNotebookFormulario, ActualizarNotebookFormulario
from django.contrib.auth.decorators import login_required

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
@login_required
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
        
            return redirect('notebooks')
        else:
            formulario_de_celulares = CrearCelularFormulario()
            return render(request, 'inicio/crear_celular.html', {'formulario_de_celulares': formulario_de_celulares})
        
    formulario_de_celulares = CrearCelularFormulario()
    return render(request, 'inicio/crear_celular.html', {'formulario_de_celulares': formulario_de_celulares})


#ELIMINAR   

@login_required 
def eliminar_notebook(request, notebook_id): 
    paleta_a_eliminar = Notebook.objects.get(id=notebook_id)
    paleta_a_eliminar.delete()
    return redirect("notebooks")   

@login_required    
def actualizar_notebook(request, notebook_id):
    notebook_a_actualizar = Notebook.objects.get(id=notebook_id)
    
    if request.method == "POST":
        formulario = ActualizarNotebookFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data    

            notebook_a_actualizar.marca = info_nueva.get('marca')
            notebook_a_actualizar.descripcion = info_nueva.get('descripcion')
            notebook_a_actualizar.año = info_nueva.get('año')
            
            notebook_a_actualizar.save()
            return redirect('notebooks')
        else:
            return render(request, 'inicio/actualizar_notebook.html', {'formulario': formulario})
    
    
    formulario = ActualizarNotebookFormulario(initial={'marca': notebook_a_actualizar.marca, 'año': notebook_a_actualizar.año, 'descripcion': notebook_a_actualizar.descripcion })
    return render(request, 'inicio/actualizar_notebook.html', {'formulario': formulario})

#DETALLE DE NOTEBOOK   
def detalle_notebook(request, notebook_id):
    notebook = Notebook.objects.get(id=notebook_id)
    return render(request,'inicio/detalle_notebook.html', {'notebook': notebook})
    
