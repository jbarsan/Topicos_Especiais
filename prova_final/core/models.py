from django.db import models


# Create your models here.

class Acao(models.Model):
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=4)

    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.sigla)


class Cotacao(models.Model):
    acao = models.ForeignKey(Acao)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{0}/{1} - {2}'.format(self.acao.sigla, self.valor, self.data)
