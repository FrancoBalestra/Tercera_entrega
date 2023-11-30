from django.urls import path
from inicio.views import inicio, notebooks, crear_notebook, crear_celular, eliminar_notebook, actualizar_notebook, detalle_notebook

urlpatterns = [
    path('', inicio, name='inicio'),
    path('notebook/', notebooks, name='notebooks'),
    path('notebook/crear/', crear_notebook, name='crear_notebook'),
    #path('celular/crear/', crear_celular, name='crear_celular'), 
    path('notebook/<int:notebook_id>/eliminar/', eliminar_notebook, name='eliminar_notebook'),
    path('notebook/<int:notebook_id>/actualizar/', actualizar_notebook, name='actualizar_notebook'),
    path('notebook/<int:notebook_id>/', detalle_notebook, name='detalle_notebook'),
]


