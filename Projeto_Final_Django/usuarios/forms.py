from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    nome_usuario = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    matricula = forms.CharField(required=True)
    telefone = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_mensagem('Verifique seus campos.')
            valid = False

        user_exists = User.objects.filter(username=self.cleaned_data['nome_usuario']).exists()
        if user_exists:
            adiciona_mensagem('Já existe um usuário cadastrado com esse nome.')
            valid = False
        return valid


class ResetarUsuarioForm(forms.Form):
    nome_usuario = forms.CharField(required=True)
    senha = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(ResetarUsuarioForm, self).is_valid():
            self.adiciona_mensagem('Verifique seus campos.')
            valid = False

        user_exists = User.objects.filter(username=self.cleaned_data['nome_usuario']).exists()
        if not user_exists:
            adiciona_mensagem('Nome de usuário não encontrado.')
            valid = False
        return valid


def adiciona_mensagem(self, msg):
    errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
    errors.append(msg)
