from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import GameCategory
from .models import Game
from .models import Player
from .models import Score


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
                                                 slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'game_category',
            'name',
            'release_date',
            'played'
        )


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('url', 'pk', 'name', 'games')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(),
                                        slug_field='name')
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                          slug_field='name')

    class Meta:
        model = Score
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'scores',
        )

