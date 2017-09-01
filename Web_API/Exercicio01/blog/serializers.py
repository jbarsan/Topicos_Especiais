from rest_framework import serializers
from .models import *


# class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['url',
                  'id',
                  'lat',
                  'lng']


# class AddressSerializer(serializers.HyperlinkedModelSerializer):
# Erro esquisito aqui 8-(
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['url',
                  'id',
                  'street',
                  'suite',
                  'city',
                  'zipcode',
                  'geo']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url',
                  'id',
                  'username',
                  'name',
                  'email',
                  'address']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Post
        fields = ['url',
                  'id',
                  'title',
                  'body',
                  'user']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['url',
                  'id',
                  'name',
                  'email',
                  'body',
                  'post']


# Listar uma postagem individual junto com o nome do usuário e seus comentários
class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['url',
                  'id',
                  'title',
                  'body',
                  'user',
                  'comments']


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url',
                  'id',
                  'username',
                  'email',
                  'name',
                  'address',
                  'posts']
