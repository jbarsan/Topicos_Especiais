from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required


# Create your views here.


def get_perfil_logado(request):
    return request.user.perfil


def index(request):
    return render(request, 'index.html')


def lista_alvaras(request):
    alvaras = AlvaraConstrucao.objects.all()
    contexto = {'alvaras': alvaras}
    return render(request, 'lista_alvaras.html', contexto)


def lista_autos(request):
    autos = AutoRegularizacao.objects.all()
    contexto = {'autos': autos}
    return render(request, 'lista_autos.html', contexto)


def lista_habitese(request):
    habiteses = HabiteSe.objects.all()
    contexto = {'habiteses': habiteses}
    return render(request, 'lista_habitese.html', contexto)


class CadastrarAlvaraView(View):
    template = 'cadastrar_alvara.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        formulario = CadastrarAlvaraForm(request.POST)

        if formulario.is_valid():
            dados = formulario.cleaned_data
            requerente = Requerente.objects.filter(nome_requerente=dados['nome_requerente'])
            endereco_obra = EnderecoObra.objects.filter(logradouro=dados['logradouro'],
                                                        numero=dados['numero'],
                                                        bairro=dados['bairro'])

            alvara = AlvaraConstrucao(
                num_alvara=dados['numero_servico'],
                ano_alvara=dados['ano_servico'],
                num_processo=dados['num_processo'],
                requerente=requerente,
                endereco_obra=endereco_obra,
                area_terreno=dados['area_terreno'],
                area_construida=dados['area_construida'],
                observacao=dados['observacao'],
                data_alvara=dados['data_alvara'],
                resp_tecnico=dados['resp_tecnico'])
            alvara.save()
            return redirect('index')

        contexto = {'formulario': formulario}
        return render(request, 'cadastrar_alvara.html', contexto)


class CadastrarAutoView(View):
    template = 'cadastrar_auto.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        formulario = CadastrarAlvaraForm(request.POST)

        if formulario.is_valid():
            dados = formulario.cleaned_data
            requerente = Requerente.objects.filter(nome_requerente=dados['requerente'])
            endereco_obra = EnderecoObra.objects.filter(logradouro=dados['logradouro'],
                                                        numero=dados['numero'],
                                                        bairro=dados['bairro'])

            auto = AutoRegularizacao(
                num_auto=dados['numero_servico'],
                ano_auto=dados['ano_servico'],
                num_processo=dados['num_processo'],
                requerente=requerente,
                endereco_obra=endereco_obra,
                area_terreno=dados['area_terreno'],
                area_construida=dados['area_construida'],
                observacao=dados['observacao'],
                data_auto=dados['data_alvara'],
                resp_tecnico=dados['resp_tecnico'])
            auto.save()
            return redirect('index')

        contexto = {'formulario': formulario}
        return render(request, 'cadastrar_auto.html', contexto)



class CadastrarHabiteseView(View):
    template = 'cadastrar_habitese.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        formulario = CadastrarAlvaraForm(request.POST)

        if formulario.is_valid():
            dados = formulario.cleaned_data
            requerente = Requerente.objects.filter(nome_requerente=dados['requerente'])
            endereco_obra = EnderecoObra.objects.filter(logradouro=dados['logradouro'],
                                                        numero=dados['numero'],
                                                        bairro=dados['bairro'])

            habitese = HabiteSe(
                num_habitese=dados['numero_servico'],
                ano_habitese=dados['ano_servico'],
                num_processo=dados['num_processo'],
                requerente=requerente,
                endereco_obra=endereco_obra,
                area_terreno=dados['area_terreno'],
                area_construida=dados['area_construida'],
                alvara_construcao=dados['num_alvara'],
                auto_regularizacao=dados['num_auto'],
                observacao=dados['observacao'],
                data_habitese=dados['data_alvara'],
                resp_tecnico=dados['resp_tecnico'])
            habitese.save()
            return redirect('index')

        contexto = {'form': formulario}
        return render(request, 'cadastrar_habitese.html', contexto)
