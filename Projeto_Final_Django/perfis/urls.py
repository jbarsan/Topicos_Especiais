from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.perfil, name='perfil'),
    url(r'^perfil/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
]