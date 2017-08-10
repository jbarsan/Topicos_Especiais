from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import RegistrarUsuarioForm
from .forms import ResetarUsuarioForm
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
            usuario = User.objects.create(first_name=dados['nome'],
                                          username=dados['nome_usuario'],
                                          email=dados['email'],
                                          password=dados['senha'])

            perfil = Perfil(nome=dados['nome'],
                            matricula=dados['matricula'],
                            telfone=dados['telefone'],
                            usuario=usuario)
            perfil.save()
            return redirect('index')

        contexto = {'form': form}
        return render(request, 'registrar.html', contexto)


def trocar_senha(self, perfil_id, nova_senha):
    perfil = Perfil.objects.get(id=perfil_id)
    usuario = User.objects.get(username=perfil.usuario.username)
    usuario.set_password(nova_senha)

    return redirect('login')
