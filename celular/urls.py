from django.urls import path
from celular.views import ListadoCelulares, CrearCelular, ActualizarCelular, EliminarCelular, DetalleCelular

urlpatterns = [
    path('celulares/', ListadoCelulares.as_view(), name='celulares'),
    path('celulares/crear/', CrearCelular.as_view(), name='crear_celular'),
    path('celulares/<int:pk>/', DetalleCelular.as_view(), name='detalle_celular'),
    path('celulares/<int:pk>/actualizar', ActualizarCelular.as_view() , name='actualizar_celular'),
    path('celulares/<int:pk>/eliminar', EliminarCelular.as_view(), name='eliminar_celular'),
    ]