from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.list_acoes, name='list_acoes'),
    url(r'^acao/(?P<pk>[0-9]+)/$', views.cotacao_detail, name='detail_cotacao'),

]
