from django.urls import path
from inicio.views import inicio, notebooks, crear_notebook, crear_celular, crear_tablet 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('notebook/', notebooks, name='notebooks'),
    path('notebook/crear/', crear_notebook, name='crear_notebook'),
    path('celular/crear/', crear_celular, name='crear_celular'),
    path('tablet/crear/', crear_tablet, name='crear_tablet'),
]


