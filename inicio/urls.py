from django.urls import path
from inicio.views import inicio, notebooks, crear_notebook

urlpatterns = [
    path('', inicio, name='inicio'),
    path('notebook/', notebooks, name='notebooks'),
    path('notebook/crear/', crear_notebook, name='crear_notebook')
]


