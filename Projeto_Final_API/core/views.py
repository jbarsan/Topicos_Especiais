from .serializers import *
import rest_framework_filters as filters
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers
from django.contrib.auth.models import User


# Create your views here.
# --- FILTROS ---#

# Para filtrar os dados, estou usando o django-rest-framework-filters, que um é
# uma extensão do Django REST framework e do Django-filter que facilita o filtro em todos os relacionamentos.
# Na variável 'fields', é possível especificar o tipo de argumento que será feita na consulta, como 'exacts', 'in',
# 'startswith' e todas as outras opções dos field-lookups do Django. Esses argumentos precisam ser checados, pois podem
# ser diferentes de acordo com o banco de dados utilizado.
# Doc.: https://docs.djangoproject.com/pt-br/1.11/ref/models/querysets/#field-lookups
# Doc.: https://github.com/philipn/django-rest-framework-filters

class CidadeFilter(filters.FilterSet):
    class Meta:
        model = Cidade
        fields = {'nome_cidade': ['icontains'],
                  'estado': ['exact']
                  }


class BairroFilter(filters.FilterSet):
    cidade = filters.RelatedFilter(CidadeFilter, name='cidade', queryset=Cidade.objects.all())

    class Meta:
        model = Bairro
        fields = {'nome_bairro': ['icontains']}



class RequerenteFilter(filters.FilterSet):
    class Meta:
        model = Requerente
        fields = {'nome': ['icontains'],
                  'cpf': ['exact']}
        


class RespTecFilter(filters.FilterSet):
    class Meta:
        model = ResponsavelTecnico
        fields = {'nome': ['icontains']}


class AlvaraFilter(filters.FilterSet):
    requerente = filters.RelatedFilter(RequerenteFilter, name='requerente', queryset=Requerente.objects.all())

    class Meta:
        model = AlvaraConstrucao
        fields = {'numero': ['exact'],
                  'ano': ['exact'],
                  'num_processo': ['exact'],
                  'end_obra': ['icontains']
                  }


class AutoFilter(filters.FilterSet):
    requerente = filters.RelatedFilter(RequerenteFilter, name='requerente', queryset=Requerente.objects.all())

    class Meta:
        model = AutoRegularizacao
        fields = {'numero': ['exact'],
                  'ano': ['exact'],
                  'num_processo': ['exact'],
                  'end_obra': ['icontains']
                  }


class HabiteSeFilter(filters.FilterSet):
    requerente = filters.RelatedFilter(RequerenteFilter, name='requerente', queryset=Requerente.objects.all())
    alvara = filters.RelatedFilter(AlvaraFilter, name='alvara', queryset=AlvaraConstrucao.objects.all())
    auto = filters.RelatedFilter(AutoFilter, name='auto', queryset=AutoRegularizacao.objects.all())

    class Meta:
        model = HabiteSe
        fields = {'numero': ['exact'],
                  'ano': ['exact'],
                  'num_processo': ['exact'],
                  'end_obra': ['icontains']
                  }


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {'username': ['icontains'],
                  'email': ['icontains']}


class AtendenteFilter(filters.FilterSet):
    user = filters.RelatedFilter(UserFilter, name='user', queryset=User.objects.all())

    class Meta:
        model = Atendente
        fields = {'matricula': ['exact']}


# ---VIEWSETS --- #
# Usar viewset no lugar das classes genericas do DRF trás uma grande facilidade
# e redução na quantidade de códigos implementandos, já que as viewsets
# implementam as 'LISTS' e 'DETAILS' por padrão, sem contar que com isso eu ganho
# os 'routers' automaticamente.

class CidadeViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista de todas as cidades cadastradas no sistema.
    read:       Retorna uma cidade.
    create:     Cria uma nova cidade no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga uma cidade.
    """
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    filter_class = CidadeFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BairroViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista de todas os bairros cadastrados no sistema.
    read:       Retorna um bairro.
    create:     Cria um novo bairro no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um bairro do banco.
    """
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    filter_class = BairroFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RequerenteViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os requerentes cadastrados no sistema.
    read:       Retorna um requerente.
    create:     Cria um novo requerente no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um requerente do banco.
    """
    queryset = Requerente.objects.all()
    serializer_class = RequerenteSerializer
    filter_class = RequerenteFilter
    permission_classes = (permissions.IsAuthenticated,)


class CargoViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os cargos cadastrados no sistema.
    read:       Retorna um cargo.
    create:     Cria um novo cargo no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um cargo do banco.
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RespTecViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os responsáveis técnicos cadastrados no sistema.
    read:       Retorna um responsável.
    create:     Cria um novo responsável no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um responsável técnico do banco.
    """
    queryset = ResponsavelTecnico.objects.all()
    serializer_class = RespTecnicoSerializer
    filter_class = RespTecFilter
    permission_classes = (permissions.IsAuthenticated,)


class AlvaraViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os alvarás cadastrados no sistema.
    read:       Retorna um alvará.
    create:     Cria um novo alvará no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um alvará do banco.
    """
    queryset = AlvaraConstrucao.objects.all()
    serializer_class = AlvaraSerializer
    filter_class = AlvaraFilter
    permission_classes = (permissions.IsAuthenticated,)


class AutoViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os autos cadastrados no sistema.
    read:       Retorna um auto.
    create:     Cria um novo auto no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um auto do banco.
    """
    queryset = AutoRegularizacao.objects.all()
    serializer_class = AutoSerializer
    filter_class = AutoFilter
    permission_classes = (permissions.IsAuthenticated,)


class HabiteSeViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os habite-ses cadastrados no sistema.
    read:       Retorna um habite-se.
    create:     Cria um novo habite-se no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um cargo do banco.
    """
    queryset = HabiteSe.objects.all()
    serializer_class = HabiteSeSerializer
    filter_class = HabiteSeFilter
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:       Retorna uma lista com todos os usuários cadastrados no sistema.
    read:       Retorna um usuário.
    create:     Cria um novo usuário no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um usuário do banco.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Somente o usuário com a flag is_superuser ativada pode visualizar os usuários.
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class AtendenteViewSet(viewsets.ModelViewSet):
    """
    list:       Retorna uma lista com todos os atendentes cadastrados no sistema.
    read:       Retorna um atendente.
    create:     Cria um novo atendente no banco do sistema.
    update:     Atualiza todos os campos.
    partial_update: Atualizar somente os campos alterados.
    delete:     Apaga um atendente do banco.
    """
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer
    filter_class = AtendenteFilter
    # Somente o usuário com a flag is_superuser ativada pode cadastrar e visualizar novos atendentes.
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def perform_create(self, serializer):
        # Cria as variaveis que recebe os dados do user
        email = self.request.POST.get('user.email')
        nome = self.request.POST.get('user.first_name')
        sobrenome = self.request.POST.get('user.last_name')
        username = self.request.POST.get('user.username')
        senha = self.request.POST.get('user.password')

        # Instanciando o user com os dados das variáveis
        # FIXME: Tem que criar o user primeiro, senão não tem como ligar com o Atendente.
        # print(self.request.POST) - DEBUG de POBRE 8-P
        user = User(first_name=nome, last_name=sobrenome, email=email, username=username)
        user.set_password(senha)
        user.save()

        # FIXME: Não precisa essa parte porque está tudo no 'serializer' (serializer_class = AtendenteSerializer)
        # matricula = self.request.data['matricula']
        # atendente = Atendente(user=user, matricula=matricula)
        # atendente.save()

        serializer.save(user=user)


# Criando uma ViewSet para o Swagger, já que o uso de viewset inviabiliza o exibição padrão
# dos urls na 'api-root'. Para isso é preciso transformar uma 'APIView' em uma 'ViewSet'.
# Ref.1: http://marcgibbons.github.io/django-rest-swagger/schema/
# Ref.2: https://stackoverflow.com/questions/30389248/how-can-i-register-a-single-view-not-a-viewset-on-my-router

class SwaggerViewSet(viewsets.ViewSet):
    """
    list:   Retorna a documentação da Api
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def list(self, request):
        generator = SchemaGenerator(title='Documentação da API')
        schema = generator.get_schema(request=request)

        return Response(schema)
