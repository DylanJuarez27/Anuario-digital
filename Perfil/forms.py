from django import forms

class Edit_data(forms.Form):
    descripcion = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 90,
            'class':'form-control',
            'style': 'resize:none;',
            'placeholder': 'Escribe tu descripcion de perfil aquí...'
        })
    )
    
    foto_perfil = forms.ImageField(required=False)
    foto_portada = forms.ImageField(required=False)
    color_perfil = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'form-control',
        }),
        initial='#f0f2f5',
        label='Color de perfil'
    )

    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label='Fecha de nacimiento'
    ) 
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto_perfil'].widget.attrs.update({
            'id': 'fotoPerfilInput',
            'class': 'd-none' 
        }) 
        self.fields['foto_portada'].widget.attrs.update({
            'id': 'fotoPortadaInput',
            'class': 'd-none' 
        }) 
