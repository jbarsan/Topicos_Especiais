# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Perfil, Convite
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    perfis = Perfil.objects.all()
    contexto = {'perfis': perfis,
                'perfil_logado': get_perfil_logado(request)}

    return render(request, 'index.html', contexto)

@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    contexto = {'perfil': perfil,
                'perfil_logado': perfil_logado,
                'ja_eh_contato': ja_eh_contato}

    return render(request, 'perfil.html', contexto)

@login_required
def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado)
    return redirect('index')


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


@login_required
def get_perfil_logado(request):
    return request.user.perfil
