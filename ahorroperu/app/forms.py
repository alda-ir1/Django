from django import forms
from .models import Producto
from .models import Objeto
from .models import Persona

#######
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni', 'celular']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido':  forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }


#######
class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre', 'precio', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

