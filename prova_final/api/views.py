from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import Acao, Cotacao
from api.serializers import AcaoSerializer, CotacaoSerializer


# Create your views here.
class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer


class CotacaoViewSet(viewsets.ModelViewSet):
    queryset = Cotacao.objects.all()
    serializer_class = CotacaoSerializer


"""
class AcaoList(generics.ListCreateAPIView):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    name = 'acao-list'


class AcaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    name = 'acao-detail'


class CotacaoList(generics.ListCreateAPIView):
    queryset = Cotacao.objects.all()
    serializer_class = CotacaoSerializer
    name = 'cotacao-list'


class CotacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cotacao.objects.all()
    serializer_class = CotacaoSerializer
    name = 'cotacao-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'acao': reverse(AcaoList.name, request=request),
            'cotacoes': reverse(CotacaoList.name, request=request),
        })

"""
