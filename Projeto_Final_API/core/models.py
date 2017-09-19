# ---Django---#
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
# ---DRF---#
from rest_framework.authtoken.models import Token
# ---EXTRAS---#
from localflavor.br.br_states import STATE_CHOICES


# Criando geradores de token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Criando funções validadoras para os campos numericos do documento
def valida_ano(valor):
    if valor < 2013:
        raise ValidationError(
            _('%(valor) não pode ser menor do que 2013'),
            params={'valor': valor},
        )


def valida_num(valor):
    if valor < 1:
        raise ValidationError(
            _('%(valor) não pode ser menor do que 1'),
            params={'valor': valor},
        )


# Para que apareça tudo bonitinho na documentação da api é preciso incluir o 'help_text'
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100,
                                   verbose_name='Nome da cidade',
                                   help_text='Informe o nome da cidade')
    estado = models.CharField(max_length=2,
                              choices=STATE_CHOICES,
                              verbose_name='Estado',
                              help_text='Informa o estado em que a cidade pertence')

    class Meta:
        ordering = ('nome_cidade',)
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome_cidade


class Bairro(models.Model):
    nome_bairro = models.CharField(max_length=200,
                                   verbose_name='Nome do bairro',
                                   help_text='Nome do bairro')
    cidade = models.ForeignKey(Cidade,
                               related_name='cidade',
                               on_delete=models.CASCADE,
                               verbose_name='Cidade',
                               help_text='Cidade em que o bairro pertence')

    class Meta:
        ordering = ('nome_bairro',)
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.nome_bairro


class Requerente(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do requerente', help_text='Nome completo do requerente')
    cpf = models.CharField(max_length=14, verbose_name='C.P.F', unique=True,
                           help_text='C.P.F no formato: 000.000.000-00')
    telefone = models.CharField(max_length=16, verbose_name='Telefone',
                                help_text='Telefone Ex.: (00) 9 0000-0000 / (00) 0000-0000')
    endereco = models.CharField(max_length=150, verbose_name='Endereço', help_text='Nome do logradouro')
    num_residencia = models.CharField(max_length=20, verbose_name='Número',
                                      help_text='Número da casa, se não possuir insira "S/N"')
    complemento = models.CharField(max_length=150, null=True, blank=True,
                                   help_text='Senão possuir complemento deixe em branco')
    bairro = models.ForeignKey(Bairro, verbose_name='Bairro', help_text='Bairro')
    cep = models.CharField(max_length=9, blank=True, null=True, help_text='Cep no formato 00000-000')
    data_cadastro = models.DateTimeField(default=timezone.now, help_text='Data e hora do cadastro')

    class Meta:
        verbose_name = 'Requerente'
        verbose_name_plural = 'Requerentes'

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição', help_text='Descrição do cargo')

    class Meta:
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.descricao


class ResponsavelTecnico(models.Model):
    nome = models.CharField(max_length=150, help_text='Nome completo do responsável técnico')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo',
                              help_text='Cargo do responsável técnico')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Responsável Técnico'
        verbose_name_plural = 'Responsáveis Técnicos'

    def __str__(self):
        text = '{}, {}'.format(self.nome, self.cargo)
        return text


class Documento(models.Model):
    ano = models.PositiveIntegerField(verbose_name='Ano do documento', validators=[valida_ano],
                                      help_text='Ano do documento a partir de 2013')
    num_processo = models.CharField(max_length=12, verbose_name='Número do processo',
                                    help_text='Número do processo no formato: 00.0000/0000')
    requerente = models.ForeignKey(Requerente, on_delete=models.CASCADE, verbose_name='Requerente',
                                   help_text='Requerente do documento')
    end_obra = models.CharField(max_length=150, verbose_name='Endereço da obra', help_text='Endereço da obra')
    num_residencia = models.CharField(max_length=20, verbose_name='Número',
                                      help_text='Número do endereço, se não possuir insira "S/N"')
    complemento = models.CharField(max_length=150, null=True, blank=True,
                                   help_text='Senão possuir complemento deixe em branco')
    bairro = models.ForeignKey(Bairro, verbose_name='Bairro', help_text='Bairro')
    cep = models.CharField(max_length=9, blank=True, null=True, help_text='Cep no formato 00000-000')
    area_terreno = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Área do terreno',
                                       help_text='Área do terreno no formato: 000.00')
    area_construida = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Área construída',
                                          help_text='Área construída no formato: 000.00')
    observacao = models.TextField(blank=True, verbose_name='Observações',
                                  help_text='Senão possuir observações deixe em branco')
    data_documento = models.DateField(verbose_name='Data do documento',
                                      help_text='Data em que o documento foi assinado. YYYY-MM-DD')
    resp_tecnico = models.ForeignKey(ResponsavelTecnico, on_delete=models.CASCADE, verbose_name='Responsável técnico',
                                     help_text='Responsável Técnico')
    data_cadastro = models.DateTimeField(default=timezone.now, help_text='Data e hora do cadastro')


class AlvaraConstrucao(Documento):
    numero = models.PositiveIntegerField(verbose_name='Número do documento', unique=True, validators={valida_num},
                                         help_text='Número do documento')

    class Meta:
        ordering = ('numero', 'ano')
        verbose_name = 'Alvará de Construção'
        verbose_name_plural = 'Alvarás de Construção'

    def __str__(self):
        return "{0}/{1} - {2}".format(self.numero, self.ano, self.requerente.nome)


class AutoRegularizacao(Documento):
    numero = models.PositiveIntegerField(verbose_name='Número do documento', unique=True, validators={valida_num},
                                         help_text='Número do documento')

    class Meta:
        verbose_name = 'Auto de Regularização'
        verbose_name_plural = 'Autos de Regularização'

    def __str__(self):
        return "{0}/{1} - {2}".format(self.numero, self.ano, self.requerente.nome)


class HabiteSe(Documento):
    numero = models.PositiveIntegerField(verbose_name='Número do documento', unique=True, validators={valida_num},
                                         help_text='Número do documento')
    alvara = models.ForeignKey(AlvaraConstrucao, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Alvará',
                               help_text='Alvará associado, senão possuir deixe em branco')
    auto = models.ForeignKey(AutoRegularizacao, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Auto',
                             help_text='Auto associado, senão possuir deixe em branco')

    class Meta:
        verbose_name = 'Habite-se'
        verbose_name_plural = 'Habite-ses'


# --- Testes --- #
class Atendente(models.Model):
    user = models.OneToOneField('auth.User', related_name='atendente', on_delete=models.CASCADE, )
    matricula = models.CharField(max_length=10, help_text='Matrícula do atendente')

    def __str__(self):
        text = '{0}, {1}, {2}'.format(self.user.get_full_name(), self.user.get_username(), self.matricula)
        return text
