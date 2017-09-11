from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from localflavor.br.br_states import STATE_CHOICES


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100, verbose_name='Nome da cidade')
    estado = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name='Estado')

    class Meta:
        ordering = ('nome_cidade',)
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome_cidade


class Bairro(models.Model):
    nome_bairro = models.CharField(max_length=200, verbose_name='Nome do bairro')
    cidade = models.ForeignKey(Cidade, related_name='cidade', on_delete=models.CASCADE, verbose_name='Cidade')

    class Meta:
        ordering = ('nome_bairro',)
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.nome_bairro


class Requerente(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    cpf = models.CharField(max_length=14, verbose_name='C.P.F', unique=True)
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, verbose_name='Endereço')
    num_residencia = models.CharField(max_length=20, verbose_name='Número')
    complemento = models.CharField(max_length=150, null=True, blank=True)
    bairro = models.ForeignKey(Bairro, verbose_name='Bairro')
    cep = models.CharField(max_length=9, blank=True, null=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Requerente'
        verbose_name_plural = 'Requerentes'

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')

    class Meta:
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.descricao


class ResponsavelTecnico(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Responsável Técnico'
        verbose_name_plural = 'Responsáveis Técnicos'

    def __str__(self):
        text = '{}, {}'.format(self.nome, self.cargo)
        return text


class Documento(models.Model):
    ano = models.PositiveIntegerField(verbose_name='Ano do documento')
    num_processo = models.CharField(max_length=12, verbose_name='Número do processo')
    requerente = models.ForeignKey(Requerente, on_delete=models.CASCADE, verbose_name='Requerente')
    end_obra = models.CharField(max_length=150, verbose_name='Endereço da obra')
    num_residencia = models.CharField(max_length=20, verbose_name='Número')
    complemento = models.CharField(max_length=150, null=True, blank=True)
    bairro = models.ForeignKey(Bairro, verbose_name='Bairro')
    cep = models.CharField(max_length=9, blank=True, null=True)
    area_terreno = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Área do terreno')
    area_construida = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Área construída')
    observacao = models.TextField(blank=True, verbose_name='Observações')
    data_documento = models.DateField(verbose_name='Data do documento')
    resp_tecnico = models.ForeignKey(ResponsavelTecnico, on_delete=models.CASCADE, verbose_name='Responsável técnico')
    data_cadastro = models.DateTimeField(default=timezone.now)


class AlvaraConstrucao(Documento):
    numero = models.PositiveIntegerField(verbose_name='Número do documento', unique=True)

    class Meta:
        ordering = ('numero', 'ano')
        verbose_name = 'Alvará de Construção'
        verbose_name_plural = 'Alvarás de Construção'

    def __str__(self):
        return "{0}/{1} - {2}".format(self.numero, self.ano, self.requerente.nome)


class AutoRegularizacao(Documento):
    numero = models.PositiveIntegerField(verbose_name='Número do documento', unique=True)

    class Meta:
        verbose_name = 'Auto de Regularização'
        verbose_name_plural = 'Autos de Regularização'

    def __str__(self):
        return "{0}/{1} - {2}".format(self.numero, self.ano, self.requerente.nome)


class HabiteSe(Documento):
    numero = models.PositiveIntegerField(verbose_name='Número do documento', unique=True)
    alvara = models.ForeignKey(AlvaraConstrucao, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Alvará')
    auto = models.ForeignKey(AutoRegularizacao, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Auto')

    class Meta:
        verbose_name = 'Habite-se'
        verbose_name_plural = 'Habite-ses'


# --- Testes --- #
class Atendente(models.Model):
    user = models.OneToOneField('auth.User', related_name='atendente', on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        text = '{0} {1}, {2}, {3}'.format(self.user.first_name, self.user.last_name, self.user.username, self.matricula)
        return text
