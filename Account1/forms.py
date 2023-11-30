from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreate(UserCreationForm):
    username = forms.CharField(label = 'Username', max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        helps_text = {key: '' for key in fields}
        
class ProfileEditForm(forms.Form):
    first_name = forms.CharField(label='nombre', required=False) 
    last_name = forms.CharField(label='apellido', required=False)
    email = forms.CharField(required=False)
    descripcion = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
        
class UserFindForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, label='')    