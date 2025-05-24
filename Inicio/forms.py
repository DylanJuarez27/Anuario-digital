from django import forms

#formulario de inicio de sesion
class login_date(forms.Form):
    username = forms.CharField(
        label="Usuario",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su usuario'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'passwordInput'
        }),
        label="Contraseña"
    )
    codigo_acceso = forms.CharField(
        label="Código de grupo",
        max_length=6,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Código de acceso',
            'id': 'CodigoAccesoInput'
        })
    )


#formulario de registro
class register_date(forms.Form):
    username = forms.CharField(
        label="Usuario",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese un usuario'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese una contraseña',
            'id': 'passwordInput'
        }),
        label="Contraseña"
    )
    codigo_acceso = forms.CharField(
        label="Código de grupo",
        max_length=6,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese un código de acceso',
            'id': 'CodigoAccesoInput'
        })
    )