from rest_framework import serializers
from .models import GameCategory
from .models import Game
from .models import Player
from .models import Score


class GameSerializer(serializers.HyperlinkedModelSerializer):
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
    pass


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    pass
