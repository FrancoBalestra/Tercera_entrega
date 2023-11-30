from django.shortcuts import render
from django.views.generic.list import ListView
from celular.models import Celular
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoCelulares(ListView):
    model = Celular
    context_object_name = 'listado_de_celulares'
    template_name='celular/celulares.html'

class CrearCelular(LoginRequiredMixin, CreateView):
    model = Celular
    template_name = "celular/crear_celular.html"
    fields = ['marca', 'modelo', 'descripcion', 'año']
    success_url = reverse_lazy('celulares')

class ActualizarCelular(LoginRequiredMixin, UpdateView):
    model = Celular
    template_name = "celular/actualizar_celular.html"
    fields = ['marca', 'modelo', 'descripcion', 'año']
    success_url = reverse_lazy('celulares')

class DetalleCelular(DetailView):
    model = Celular
    template_name = "celular/detalle_celular.html"
    
class EliminarCelular(LoginRequiredMixin, DeleteView):
    model = Celular
    template_name = "celular/eliminar_celular.html"
    success_url = reverse_lazy('celulares')