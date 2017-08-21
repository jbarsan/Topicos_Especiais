from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')

    # Verifica se o valor é vazio
    def is_empty(self, valor):
        if valor == '' or valor is None:
            '''
            Chamando o ValidationError do serializers, assim diferencia
            do erro de validação interno do django.
            http://www.django-rest-framework.org/api-guide/exceptions/#validationerror
            '''
            raise serializers.ValidationError("Todos os campos devem ser preenchidos.")
        return valor

    # Verifica se um jogo já está cadastrado
    def is_registered(self, valor):
        if Game.objects.filter(name=valor):
            raise serializers.ValidationError("Este jogo já está cadastrado.")

    # Valida data
    def validate_release_date(self, release_date):
        return self.is_empty(release_date)

    # Valida categoria
    def validate_game_category(self, game_category):
        return self.is_empty(game_category)

    # Valida Nome
    def validate_name(self, nome):
        self.is_registered(nome)
        return self.is_empty(nome)
