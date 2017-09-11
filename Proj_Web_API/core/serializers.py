from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


# ---CIDADE --- #
class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('url', 'nome_cidade', 'estado')


# --- BAIRRO --- #
class BairroSerializer(serializers.HyperlinkedModelSerializer):
    # cidade = serializers.HyperlinkedRelatedField(queryset=Cidade.objects.all(), view_name='cidade-detail')
    cidade = CidadeSerializer()

    class Meta:
        model = Bairro
        fields = ('url', 'nome_bairro', 'cidade')


# --- REQUERENTE --- #
class RequerenteSerializer(serializers.HyperlinkedModelSerializer):
    data_cadastro = serializers.ReadOnlyField()

    class Meta:
        model = Requerente
        fields = ('url', 'nome', 'cpf', 'telefone', 'endereco',
                  'num_residencia', 'complemento', 'bairro', 'cep', 'data_cadastro')


# --- CARGO --- #
class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = ('url', 'descricao')


# --- RESPONSÁVEL TÉCNICO --- #
class RespTecnicoSerializer(serializers.HyperlinkedModelSerializer):
    # Exibe os dados que vem do 'Cargo'
    cargo = serializers.HyperlinkedRelatedField(queryset=Cargo.objects.all(), view_name='cargo-detail')
    #cargo = CargoSerializer()

    class Meta:
        model = ResponsavelTecnico
        fields = ('url', 'nome', 'cargo')


# --- ALVARÁ DE CONSTRUÇÃO --- #
class AlvaraSerializer(serializers.HyperlinkedModelSerializer):
    data_cadastro = serializers.ReadOnlyField()
    requerente = serializers.HyperlinkedRelatedField(queryset=Requerente.objects.all(), view_name='requerente-detail')
    bairro = serializers.HyperlinkedRelatedField(queryset=Bairro.objects.all(), view_name='bairro-detail')
    resp_tecnico = serializers.HyperlinkedRelatedField(queryset=ResponsavelTecnico.objects.all(),
                                                       view_name='responsaveltecnico-detail')

    class Meta:
        model = AlvaraConstrucao
        fields = ('url', 'numero', 'ano', 'num_processo', 'requerente',
                  'end_obra', 'num_residencia', 'complemento', 'bairro',
                  'cep', 'area_terreno', 'area_construida', 'observacao',
                  'data_documento', 'resp_tecnico', 'data_cadastro')


# --- AUTO DE REGULARIZAÇÃO --- #
class AutoSerializer(serializers.HyperlinkedModelSerializer):
    data_cadastro = serializers.ReadOnlyField()
    requerente = serializers.HyperlinkedRelatedField(queryset=Requerente.objects.all(), view_name='requerente-detail')
    bairro = serializers.HyperlinkedRelatedField(queryset=Bairro.objects.all(), view_name='bairro-detail')
    resp_tecnico = serializers.HyperlinkedRelatedField(queryset=ResponsavelTecnico.objects.all(),
                                                       view_name='responsaveltecnico-detail')

    class Meta:
        model = AutoRegularizacao
        fields = ('url', 'numero', 'ano', 'num_processo', 'requerente',
                  'end_obra', 'num_residencia', 'complemento', 'bairro',
                  'cep', 'area_terreno', 'area_construida', 'observacao',
                  'data_documento', 'resp_tecnico', 'data_cadastro')


# --- HABITE-SE --- #
class HabiteSeSerializer(serializers.HyperlinkedModelSerializer):
    data_cadastro = serializers.ReadOnlyField()
    requerente = serializers.HyperlinkedRelatedField(queryset=Requerente.objects.all(), view_name='requerente-detail')
    bairro = serializers.HyperlinkedRelatedField(queryset=Bairro.objects.all(), view_name='bairro-detail')
    resp_tecnico = serializers.HyperlinkedRelatedField(queryset=ResponsavelTecnico.objects.all(),
                                                       view_name='responsaveltecnico-detail')
    alvara = serializers.HyperlinkedRelatedField(queryset=AlvaraConstrucao.objects.all(),
                                                 view_name='alvaraconstrucao-detail')
    auto = serializers.HyperlinkedRelatedField(queryset=AutoRegularizacao.objects.all(),
                                               view_name='autoregularizacao-detail')

    class Meta:
        model = HabiteSe
        fields = ('url', 'numero', 'ano', 'num_processo', 'requerente',
                  'end_obra', 'num_residencia', 'complemento', 'bairro',
                  'cep', 'area_terreno', 'area_construida', 'alvara', 'auto',
                  'observacao', 'data_documento', 'resp_tecnico', 'data_cadastro')


# --- USUÁRIOS --- #
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email',)


class AtendenteSerializer(serializers.HyperlinkedModelSerializer):
    # Lista todos os dados do Atendente vindo do 'User'
    user = UserSerializer()

    class Meta:
        model = Atendente
        fields = ('url', 'user', 'matricula')
