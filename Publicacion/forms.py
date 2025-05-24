from django import forms

#formulario para publicacion
class publication_user(forms.Form):
    descripcion = forms.CharField(
        max_length=1500,
        widget=forms.Textarea(attrs={
            'rows': 10,
            'cols': 100,
            'class':'form-control',
            'style': 'resize:none;',
            'placeholder': 'Escribe tu publicación aquí...'
        })
    )
    foto = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto'].widget.attrs.update({
            'id': 'fotoInput',
            'class': 'd-none' 
        })    