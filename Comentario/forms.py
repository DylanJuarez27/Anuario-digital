from django import forms

#formulario para comentario
class comment_user(forms.Form):
    contenido = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'cols': 20,
            'class':'form-control',
            'style': 'resize:none;',
            'placeholder': 'Escribe tu comentario aquí...'
        })
    )