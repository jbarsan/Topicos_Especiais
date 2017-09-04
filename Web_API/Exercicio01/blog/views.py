from django.shortcuts import render
from rest_framework.reverse import reverse  # Não é do django
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from .models import *
from .permissions import *


# Create your views here.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'usuários': reverse(ListaUsuario.name, request=request),
            'posts': reverse(ListaPost.name, request=request),
            'comentários': reverse(ListaComentarios.name, request=request),
            'endereços': reverse(ListaEndereco.name, request=request),
        })
        # Lembrar que o reverse é do rest_framework e não do django


class ListaUsuario(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class DetalheUsuario(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    name = 'user-detail'


class ListaPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetalhePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = 'post-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class ListaComentarios(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class DetalheComentario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        CommentIsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListaEndereco(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'


class DetalheEndereco(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListaGeolocalizacao(generics.ListCreateAPIView):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    name = 'geolocation-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class DetalheGeolocalizacao(generics.ListCreateAPIView):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    name = 'geolocation-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

