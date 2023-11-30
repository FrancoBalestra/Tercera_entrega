from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login 
from Account1.forms import UserCreate, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from Account1.models import DatosExtra


def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            user = formulario.get_user()
            login(request, user) 
            return redirect('index')  
    else:
        formulario = AuthenticationForm()      
        
    return render(request, 'Account1/login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = UserCreate(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = UserCreate()
    
    return render(request, 'Account1/registro.html', {'formulario': formulario})

@login_required
def perfil(request):
    
    datosextra, es_nuevo = DatosExtra.objects.get_or_create(user=request.user)
    
    return render(request, 'Account1/perfil.html', {})

@login_required
def editar_perfil(request):
       
    user = request.user
    
    if request.method == 'POST':
       formulario = ProfileEditForm(request.POST, request.FILES)
       
       if formulario.is_valid():
           data = formulario.cleaned_data
           
           user.first_name = data['first_name']
           user.last_name = data['last_name']
           user.email = data['email']
           user.datosextra.descripcion = data['descripcion']
           user.datosextra.avatar = data['avatar']
           
           user.save()
           user.datosextra.save()
           
           return redirect('perfil')
    else:   
        formulario = ProfileEditForm(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'descripcion': user.datosextra.descripcion,
                'avatar': user.datosextra.avatar,
            }
        )
    
    return render(request, 'Account1/editar_perfil.html', {'formulario': formulario})     
    

class password(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Account1/password.html'
    success_url = reverse_lazy('login')
