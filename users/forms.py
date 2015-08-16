# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):

    usr = forms.CharField(label="Nombre del usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class SignupForm(forms.Form):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.CharField(label="Email")
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput)