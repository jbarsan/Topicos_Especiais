from django.conf.urls import url, include
from . import views
from .views import CadastrarAlvaraView, CadastrarAutoView, CadastrarHabiteseView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^service/)/',
        include([
            url(r'^lista_alvaras/$', views.lista_alvaras, name='lista_alvaras'),
            url(r'^lista_autos/$', views.lista_autos, name='lista_autos'),
            url(r'^lista_habitese/$', views.lista_habitese, name='lista_habitese'),
            url(r'^cadastra_alvara/$', CadastrarAlvaraView.as_view(), name='cadastra_alvara'),
            url(r'^cadastra_auto/$', CadastrarAutoView.as_view(), name='cadastra_auto'),
            url(r'^cadastra_habitese/$', CadastrarHabiteseView.as_view(), name='cadastra_habitese'),
            #url(r'^busca_alvara/$', views.busca_alvara, name='busca_alvara'),
            #url(r'^busca_auto/$', views.busca_auto, name='busca_auto'),
            #url(r'^busca_habitese/$', views.busca_habitese, name='busca_habitese'),
        ])),
]

