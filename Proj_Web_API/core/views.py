from .serializers import *
from .permissions import *

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

# Create your views here.
# --- END POINT DA API --- #
"""
Usando o decorador @api_view pois aqui é uma função simples, que irá retornar uma lista 
com todos os links disponíveis na api.
"""


@api_view(['GET'])
def api_root(request):
    return Response({
        'requerentes': reverse('requerentes-list', request=request),
        'cargos': reverse('cargo-list', request=request),
        'resp. técnicos': reverse('responsaveltecnico-list', request=request),
        'alvaras': reverse('alvaraconstrucao-list', request=request),
        'autos': reverse('autoregularizacao-list', request=request),
        'habite-ses': reverse('habitese-list', request=request),
        'cidades': reverse('cidade-list', request=request),
        'bairros': reverse('bairro-list', request=request),
        'atendente': reverse('atendente-list', request=request),
    })


# ---VIEWSETS --- #
"""
Usar viewset no lugar das classes genericas do DRF trás uma grande facilidade
e redução na quantidade de códigos implementandos, já que as viewsets 
implementam as 'LISTS' e 'DETAILS' por padrão.
"""


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BairroViewSet(viewsets.ModelViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RequerenteViewSet(viewsets.ModelViewSet):
    queryset = Requerente.objects.all()
    serializer_class = RequerenteSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RespTecViewSet(viewsets.ModelViewSet):
    queryset = ResponsavelTecnico.objects.all()
    serializer_class = RespTecnicoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlvaraViewSet(viewsets.ModelViewSet):
    queryset = AlvaraConstrucao.objects.all()
    serializer_class = AlvaraSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class AutoViewSet(viewsets.ModelViewSet):
    queryset = AutoRegularizacao.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class HabiteSeViewSet(viewsets.ModelViewSet):
    queryset = HabiteSe.objects.all()
    serializer_class = HabiteSeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class AtendenteViewSet(viewsets.ModelViewSet):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


'''
# ---CIDADE --- #
class CidadeList(generics.ListAPIView):
    """
    GET: Retorna uma lista com todas as cidades cadastradas
    POST: Cadastra uma nova cidade
    """
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    name = 'cidade-list'
    permission_classes = (permissions.IsAuthenticated,)


class CidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna uma cidade da base de dados
    DELETE: Apaga uma cidade da base de dados
    PUT: Atualiza uma cidade na base de dados
    PATCH: Atualiza parcialmente uma cidade na base de dados
    """
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    name = 'cidade-detail'
    permission_classes = (permissions.IsAuthenticated,)


# --- BAIRRO --- #
class BairroList(generics.ListCreateAPIView):
    """
    GET: Retorna uma lista com todos os bairros
    POST: Cadastra um novo bairro
    """
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    name = 'bairro-list'
    permission_classes = (permissions.IsAuthenticated,)


class BairroDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um bairro da base de dados
    DELETE: Apaga um bairro da base de dados
    PUT: Atualiza um bairro na base de dados
    PATCH: Atualiza parcialmente um bairro na base de dados
    """
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    name = 'bairro-detail'
    permission_classes = (permissions.IsAuthenticated,)


# ---REQUERENTE --- #
class RequerenteList(generics.ListCreateAPIView):
    """
    GET: Retorna uma lista com todos os requerentes cadastrados
    POST: Cadastra um novo requerente na base de dados
    """
    queryset = Requerente.objects.all()
    serializer_class = RequerenteSerializer
    name = 'requerente-list'
    permission_classes = (permissions.IsAuthenticated,)


class RequerenteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um requerente da base de dados
    DELETE: Apaga um requerente da base de dados
    PUT: Atualiza um requerente na base de dados
    PATCH: Atualiza parcialmente um requerente na base de dados
    """
    queryset = Requerente.objects.all()
    serializer_class = RequerenteSerializer
    name = 'requerente-detail'
    permission_classes = (permissions.IsAuthenticated,)


# --- CARGO DO RESPONSÁVEL TÉCNICO --- #
class CargoList(generics.ListAPIView):
    """
    GET: Retorna uma lista com todos os cargos cadastrados na base de dados
    POST: Cadastra um novo cargo
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    name = 'cargo-list'
    permission_classes = (permissions.IsAuthenticated,)


class CargoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um cargo da base de dados
    DELETE: Apaga um cargo da base de dados
    PUT: Atualiza um cargo na base de dados
    PATCH: Atualiza parcialmente um cargo na base de dados
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    name = 'cargo-detail'
    permission_classes = (permissions.IsAuthenticated,)


# --- RESPONSÁVEL TÉCNICO --- #
class RespTecList(generics.ListCreateAPIView):
    """
    GET: Retorna uma lista com todos os Resp. Técnicos cadastrados
    POST: Cadastra um novo Resp. Técnico
    """
    queryset = ResponsavelTecnico.objects.all()
    serializer_class = RespTecnicoSerializer
    name = 'responsaveltecnico-list'
    permission_classes = (permissions.IsAuthenticated,)


class RespTecDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um resp. técnico da base de dados
    DELETE: Apaga um resp. técnico da base de dados
    PUT: Atualiza um resp. técnico na base de dados
    PATCH: Atualiza parcialmente um resp. técnico na base de dados
    """
    queryset = ResponsavelTecnico.objects.all()
    serializer_class = RespTecnicoSerializer
    name = 'responsaveltecnico-detail'
    permission_classes = (permissions.IsAuthenticated,)


# --- ALVARÁ DE CONSTRUÇÃO --- #
class AlvaraList(generics.ListCreateAPIView):
    """
    GET: Retorna uma lista com todos os alvarás cadastrados
    POST: Cadastra um novo alvará
    """
    queryset = AlvaraConstrucao.objects.all()
    serializer_class = AlvaraSerializer
    name = 'alvaraconstrucao-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AlvaraDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um alvará da base de dados
    DELETE: Apaga um alvará da base de dados
    PUT: Atualiza um alvará na base de dados
    PATCH: Atualiza parcialmente um alvará na base de dados
    """
    queryset = AlvaraConstrucao.objects.all()
    serializer_class = AlvaraSerializer
    name = 'alvaraconstrucao-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# --- AUTO DE REGULARIZAÇÃO --- #
class AutoList(generics.ListCreateAPIView):
    """
    GET: Retorna uma lista com todos os autos de regularização cadastrados
    POST: Cadastra um novo auto de regularização
    """
    queryset = AutoRegularizacao.objects.all()
    serializer_class = AutoSerializer
    name = 'autoregularizacao-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AutoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um auto de regularização da base de dados
    DELETE: Apaga um auto de regularização da base de dados
    PUT: Atualiza um auto de regularização na base de dados
    PATCH: Atualiza parcialmente um auto de regularização na base de dados
    """
    queryset = AutoRegularizacao.objects.all()
    serializer_class = AutoSerializer
    name = 'autoregularizacao-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# --- HABITE-SE --- #
class HabiteSeList(generics.ListCreateAPIView):
    """
    GET: Retorna uma lista com todos os habite-ses
    POST: Cadastra um novo habite-se
    """
    queryset = HabiteSe.objects.all()
    serializer_class = HabiteSeSerializer
    name = 'habitese-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HabiteSeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna um habite-se da base de dados
    DELETE: Apaga um habite-se da base de dados
    PUT: Atualiza um habite-se na base de dados
    PATCH: Atualiza parcialmente um habite-se na base de dados
    """
    queryset = HabiteSe.objects.all()
    serializer_class = HabiteSeSerializer
    name = 'habitese-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# --- USUÁRIOS --- #
class AtendenteList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AtendenteSerializer
    name = 'atendente-list'
    permission_classes = (permissions.IsAuthenticated,)


class AtendenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AtendenteDetailSerializer
    name = 'atendente-detail'
    permission_classes = (permissions.IsAuthenticated,)
'''
