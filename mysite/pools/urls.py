from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.exibir, name='exibir'),
    url(r'^question/(?P<question_id>\d+)/results$', views.results, name='resultados'),
    url(r'^question/(?P<question_id>\d+)/vote$', views.vote, name='voto'),
]
