from django.shortcuts import render, get_object_or_404
from core.models import Cotacao, Acao


# Create your views here.
def list_acoes(request):
    acoes = Acao.objects.all()
    return render(request, 'core/acoes.html', {'acoes': acoes})


def cotacao_detail(request, pk):
    cotacao = Cotacao.objects.filter(acao=pk)

    return render(request, 'core/detail.html', {'cotacoes': cotacao})