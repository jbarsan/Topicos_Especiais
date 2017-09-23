from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import *


rota = DefaultRouter()
rota.register(r'acao', AcaoViewSet)
rota.register(r'cotacao', CotacaoViewSet)

urlpatterns = [
    url(r'^', include(rota.urls)),
    #url(r'^acao/', AcaoList.as_view(), name=AcaoList.name),
    #url(r'^acao/(?P<pk>[0-9]+)/$', AcaoDetail.as_view(), name=AcaoDetail.name),
    #url(r'^cotacao/', CotacaoList.as_view(), name=CotacaoList.name),
    #url(r'^cotacao/(?P<pk>[0-9]+)/$', CotacaoDetail.as_view(), name=CotacaoDetail.name),
    #url(r'^', ApiRoot.as_view(), name=ApiRoot.name),
]