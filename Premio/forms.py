from django import forms
from Categoria.models import Categoria

class create_prize_user(forms.Form):
      nombre = forms.CharField(
         max_length=20,
         widget=forms.TextInput(attrs={
            'class': 'form-control form-style',
            'placeholder': 'Ingresa tu nombre'
         })
      )

      descripcion = forms.CharField(
         max_length=20,
         widget=forms.TextInput(attrs={
            'class': 'form-control form-style',
            'placeholder': 'Ingresa una descripcion'
         })
     )
      categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecciona una categoría",
        widget=forms.Select(attrs={'class': 'form-select custom-select'})
      )
