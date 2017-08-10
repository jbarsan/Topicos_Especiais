# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil


# Create your views here.

class RegistrarUsuarioView(View):
    template = 'registrar.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data
            usuario = User.objects.create(username=dados['nome'],
                                          email=dados['email'],
                                          password=dados['senha'])

            perfil = Perfil(nome=dados['nome'],
                            telefone=dados['telefone'],
                            nome_empresa=dados['nome_empresa'],
                            usuario=usuario)
            perfil.save()
            return redirect('index')

        return render(request, self.template, {'form': form})
