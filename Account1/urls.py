from django.urls import path
from django.contrib.auth.views import LogoutView
from Account1 import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', LogoutView.as_view(template_name='Account1/logout.html'), name='logout'),
    path('registro/', views.registro, name='registrarse'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/password', views.password.as_view(), name='password'),
]
