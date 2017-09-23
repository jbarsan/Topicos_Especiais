from rest_framework import serializers
from core.models import Acao, Cotacao


class CotacaoSerializer(serializers.HyperlinkedModelSerializer):
    # acao = serializers.HyperlinkedRelatedField(queryset=Acao.objects.all(), view_name='acao-detail')
    acao = serializers.SlugRelatedField(queryset=Acao.objects.all(), slug_field='nome')

    class Meta:
        model = Cotacao
        fields = ('url', 'id', 'acao', 'data', 'valor',)


class AcaoSerializer(serializers.HyperlinkedModelSerializer):
    cotacoes = CotacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Acao
        fields = ('url', 'id', 'nome', 'sigla', 'cotacoes',)
