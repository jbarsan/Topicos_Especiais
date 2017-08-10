from django.shortcuts import render
from .models import Perfil
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def perfil(request):
    perfis = Perfil.objects.all()
    contexto = {'perfis': perfis,
                'perfil_logado': get_perfil_logado(request)}

    return render(request, 'index.html', contexto)


@login_required
def get_perfil_logado(request):
    return request.user.perfil


@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    contexto = {'perfil': perfil,
                'perfil_logado': get_perfil_logado(request)}

    return render(request, 'perfil.html', contexto)
