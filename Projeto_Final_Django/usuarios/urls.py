from django.conf.urls import url
from .views import RegistrarUsuarioView
from django.contrib.auth import views

urlpatterns = [
    url(r'^registrar/$', RegistrarUsuarioView.as_view(),name='registrar'),
    url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name='logout'),
    url(r'^recuperar_senha/$', views.LogoutView.as_view(template_name='resetar_senha.html'), name='resetar_senha'),
]