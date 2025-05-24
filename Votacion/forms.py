from django import forms
from django.core.exceptions import ValidationError
from Premio.models import Premio
from Perfil.models import Perfil


class create_votation_user(forms.Form):
      premio = forms.ModelChoiceField(
        queryset=Premio.objects.all(),
        empty_label="Selecciona un premio",
        widget=forms.Select(attrs={'class': 'form-select custom-select'})
      )
      perfiles_nominados = forms.ModelMultipleChoiceField(
         queryset=Perfil.objects.all(),
         widget=forms.SelectMultiple(attrs={
             'class': 'form-control select2',  
         })
      )    

      fecha_fin = forms.DateTimeField(
        required=True,
        input_formats=['%Y-%m-%dT%H:%M'],  
        widget=forms.DateTimeInput(attrs={
          'type': 'datetime-local',
          'class': 'form-control'
        })
      )
      
      def clean_perfiles_nominados(self):
        data = self.cleaned_data['perfiles_nominados']
        if len(data) < 2:
            raise ValidationError("Debes seleccionar al menos dos perfiles.")
        return data      