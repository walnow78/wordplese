# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm, SignupForm
from django.views.generic import View
from django.contrib.auth.models import User

class LoginView(View):

    def get(self, request):
        error_message = []
        form = LoginForm()

        form = LoginForm()

        context = {
            'errors': error_message,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_message = []
        form = LoginForm()
        # paso al formulario los datos con la petición.
        form = LoginForm(request.POST)

        if form.is_valid():

            # recupero los datos del usuario del formulario. en cleaned_data, tengo los campos normalizados.
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')

            # busco el usuario, si existe, me devuelve el usuario o un nulo en caso de que no lo encuentre.
            user = authenticate(username=username, password=password)
            if user is None:
                error_message.append('El usuario o la contraseña es incorrecta')
            else:
                if user.is_active:
                    # El usuario existe y está activo así que lo autentifico.
                    django_login(request, user)
                    # Por si he llegado al login desde una pagina que usa el decorador, me voy donde
                    # me indica el parametro 'next'
                    return redirect(request.GET.get('next', 'home'))
                else:
                    error_message.append('El usuario no está activo')

        context = {
            'errors': error_message,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('home')


class SignupView(View):

    def get(self, request):
        error_messages = []
        form = SignupForm()
        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        error_messages = []
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('usr')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pwd')
            blog_name = form.cleaned_data.get('blog_name')
            users = User.objects.filter(username=username)
            if len(users) == 0:
                new_user = User()
                new_user.username = username
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.email = email
                new_user.set_password(password)
                new_user.save()

                return redirect('home')
            else:
                error_messages.append('El username {0} ya existe. Pruebe con otro'.format(username))

        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)
