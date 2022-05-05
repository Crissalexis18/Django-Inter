from dataclasses import fields
from django import forms
from articulos.models import Articulos, Categoria, DetalleArticulos

class FormArticulo(forms.ModelForm):
        
    class Meta:
        model = Articulos
        # fields = ['nombre','genero','stock']
        fields = '__all__'
        # exclude = 'stock'
        
        widgets = {
         
            'nombre': forms.TextInput(attrs= {'class':'form-control'}),
            'decripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }
        
class FormCategoria(forms.ModelForm):
        
    class Meta:
        model = Categoria
        # fields = ['nombre','genero','stock']
        fields = '__all__'
        # exclude = 'stock'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            
        }


class FormDetalleArticulos(forms.ModelForm):
        
    class Meta:
        model = DetalleArticulos
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),  
        }
        
        
# class FormEjemplo(forms.Form):
#     pass
    