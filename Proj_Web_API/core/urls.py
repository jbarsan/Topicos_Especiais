from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
# Inserindo a biblioteca padrão do DRF para documentação
from rest_framework.documentation import include_docs_urls, get_docs_view
from rest_framework_swagger.views import get_swagger_view

docs = include_docs_urls(title='Documentação da API', description='Documentação gerada com o proprio DRF', )
swagger = get_swagger_view(title='Documentação da API')


# Definindo rotas automaticamente com o DefaultRouter do DRF.
# Isto é possível porque estou usando viewsets nas views.
# Isso facilita, pois as urls são geradas automaticamente, não
# preciso repetir código.
#
# Ref.1: http://www.django-rest-framework.org/api-guide/routers/#routers
# Ref.2: http://www.tomchristie.com/rest-framework-2-docs/tutorial/6-viewsets-and-routers

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
# router.register(r'docs', swagger, base_name='docs')
# router.register(r'docs', docs, base_name='docs')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', docs, name='docs'),
]