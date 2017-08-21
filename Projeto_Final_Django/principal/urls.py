from django.conf.urls import url
from principal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^docs/$', views.documentos, name='documentos'),
    url(r'^docs/add_alvara', views.add_alvara, name='add_alvara'),
    url(r'^docs/add_auto', views.add_auto, name='add_auto'),
]
