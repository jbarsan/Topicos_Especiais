# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):

        valid = True

        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_mensagem('Verifique seus campos.')
            valid = False

        user_exists = User.objects.filter(username=self.cleaned_data['nome']).exists()
        if user_exists:
            self.adiciona_mensagem('Já existe um usuário cadastrado com esse nome.')
            valid = False

        return valid

    def adiciona_mensagem(self, mensagem):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,
                                         forms.utils.ErrorList())

        errors.append(mensagem)
