# -*- coding: utf-8 -*-

from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistroFormulario(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput()
    )
    password2 = forms.CharField(
        label = 'Password (Again)',
        widget = forms.PasswordInput()
    )

    def limpiar_password2(self):
        if 'password1' in self.clean_data:
            password1 = self.clean_data['password1']
            password2 = self.clean_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Contraseñas no coinciden')

    def limpiar_usuario(self):
        usuario = self.clean_data['usuario']
        if not re.search(r'^\w+$', usuario):
            raise forms.ValidationError('Usuario solo puede tener carácter alfanumérico y guión bajo')
        try:
            User.objects.get(usuario=usuario)
        except ObjectDoesNotExist:
            return usuario
        raise forms.ValidationError('Usuario ya existe')

class GuardarMarcadorFormulario(forms.Form):
    url = forms.URLField(
        label  = 'URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    titulo = forms.CharField(
        label = 'Titulo',
        widget=forms.TextInput(attrs={'size': 64})
    )
    tags = forms.CharField(
        label = 'Tags',
        required = False,
        widget=forms.TextInput(attrs={'size': 64})
    )