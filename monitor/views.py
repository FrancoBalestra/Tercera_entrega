from django.shortcuts import render
from django.views.generic.list import ListView
from monitor.models import Monitor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoMonitores(ListView):
    model = Monitor
    context_object_name = 'listado_de_monitores'
    template_name='monitor/monitores.html'

class CrearMonitor(LoginRequiredMixin, CreateView):
    model = Monitor
    template_name = "monitor/crear_monitor.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_de_creacion']
    success_url = reverse_lazy('monitores')

class ActualizarMonitor(LoginRequiredMixin, UpdateView):
    model = Monitor
    template_name = "monitor/actualizar_monitor.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_de_creacion']
    success_url = reverse_lazy('monitores')

class DetalleMonitor(DetailView):
    model = Monitor
    template_name = "monitor/detalle_monitor.html"
    
class EliminarMonitor(LoginRequiredMixin, DeleteView):
    model = Monitor
    template_name = "monitor/eliminar_monitor.html"
    success_url = reverse_lazy('monitores')
