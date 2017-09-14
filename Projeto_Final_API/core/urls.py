from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# Definindo rotas automaticamente com o DefaultRouter do DRF.
# Isto é possível porque estou usando viewsets nas views.
# Isso facilita, pois as urls são geradas automaticamente, não
# preciso repetir código e usando o 'defaultrouter' eu ganho o api-root.
#
# Ref.1: http://www.django-rest-framework.org/api-guide/routers/#routers
# Ref.2: http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
# Ref.3: http://www.tomchristie.com/rest-framework-2-docs/tutorial/6-viewsets-and-routers

# Definindo uma rota
router = DefaultRouter()
router.register(r'requerente', views.RequerenteViewSet)
router.register(r'resp_tecnico', views.RespTecViewSet)
router.register(r'alvara', views.AlvaraViewSet)
router.register(r'auto', views.AutoViewSet)
router.register(r'habite_se', views.HabiteSeViewSet)
router.register(r'cidade', views.CidadeViewSet)
router.register(r'bairro', views.BairroViewSet)
router.register(r'cargo', views.CargoViewSet)
router.register(r'atendente', views.AtendenteViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'documentacao', views.SwaggerViewSet, base_name='swagger')

urlpatterns = [
    url(r'^', include(router.urls)),
]
