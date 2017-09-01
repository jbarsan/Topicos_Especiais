from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(ListaUser.name, request=request),
            'posts': reverse(ListaPost.name, request=request),
            'comments': reverse(ListaComentarios.name, request=request)
        })
    # Lembrar que o reverse é do rest_framework e não do django


class ListaUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class DetalheUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    name = 'user-detail'


class ListaPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'


class DetalhePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = 'post-detail'


class ListaComentarios(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class DetalheComentario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


