from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', ApiRoot.as_view(), name='root'),
    url(r'^users/$', ListaUser.as_view(), name=ListaUser.name),
    url(r'^users/(?P<pk>[0-9]+)/$', DetalheUser.as_view(), name=DetalheUser.name),
    url(r'^posts/$', ListaPost.as_view(), name=ListaPost.name),
    url(r'^posts/(?P<pk>[0-9]+)/$', DetalhePost.as_view(), name=DetalhePost.name),
    url(r'^comments/$', ListaComentarios.as_view(), name=ListaComentarios.name),
    url(r'^comments/(?P<pk>[0-9]+)/$', DetalheComentario.as_view(), name=DetalheComentario.name),
]