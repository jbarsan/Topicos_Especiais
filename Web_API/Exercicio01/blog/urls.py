from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', ApiRoot.as_view(), name='root'),
    url(r'^users/$', ListaUsuario.as_view(), name=ListaUsuario.name),
    url(r'^users/(?P<pk>[0-9]+)/$', DetalheUsuario.as_view(), name=DetalheUsuario.name),
    url(r'^posts/$', ListaPost.as_view(), name=ListaPost.name),
    url(r'^posts/(?P<pk>[0-9]+)/$', DetalhePost.as_view(), name=DetalhePost.name),
    url(r'^comments/$', ListaComentarios.as_view(), name=ListaComentarios.name),
    url(r'^comments/(?P<pk>[0-9]+)/$', DetalheComentario.as_view(), name=DetalheComentario.name),
    url(r'^address/$', ListaEndereco.as_view(), name=ListaEndereco.name),
    url(r'^address/(?P<pk>[0-9]+)/$', DetalheEndereco.as_view(), name=DetalheEndereco.name),
    url(r'geolocation/$', ListaGeolocalizacao.as_view(), name=ListaGeolocalizacao.name),
    url(r'^geolocation/(?P<pk>[0-9]+)/$', DetalheGeolocalizacao.as_view(), name=DetalheGeolocalizacao.name),
]