from django.urls import path
from monitor.views import ListadoMonitores, CrearMonitor, ActualizarMonitor, EliminarMonitor, DetalleMonitor

urlpatterns = [
    path('monitores/', ListadoMonitores.as_view(), name='monitores'),
    path('monitores/crear/', CrearMonitor.as_view(), name='crear_monitor'),
    path('monitores/<int:pk>/', DetalleMonitor.as_view(), name='detalle_monitor'),
    path('monitores/<int:pk>/actualizar', ActualizarMonitor.as_view() , name='actualizar_monitor'),
    path('monitores/<int:pk>/eliminar', EliminarMonitor.as_view(), name='eliminar_monitor'),
    ]
