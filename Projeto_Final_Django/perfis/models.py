from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=255, null=False)
    matricula = models.CharField(max_length=30, null=True)
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email

