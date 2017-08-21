from django.db import models


# Create your models here.
class Estado(models.Model):
    nome_estado = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nome_estado


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name='estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cidade


class Bairro(models.Model):
    nome_bairro = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, related_name='cidade', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_bairro


class CPF(models.Model):
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.cpf


class EnderecoObra(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{0} {1}, {2}, {3}".format(self.logradouro, self.numero, self.bairro.nome_bairro,
                                          self.cidade.nome_cidade)


class EnderecoRequerente(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{0} {1}, {2}, {3}".format(self.logradouro, self.numero, self.bairro.nome_bairro,
                                          self.cidade.nome_cidade)


class Requerente(models.Model):
    nome_requerente = models.CharField(max_length=100)
    cpf = models.OneToOneField(CPF, related_name='cpf_requerente', on_delete=models.CASCADE)
    endereco = models.ForeignKey(EnderecoRequerente, related_name='endereco_requerente')
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome_requerente


class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class ResponsavelTecnico(models.Model):
    nome_resp_tecnico = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_resp_tecnico


class AlvaraConstrucao(models.Model):
    num_alvara = models.IntegerField(unique=True)
    ano_alvara = models.IntegerField()
    num_processo = models.CharField(max_length=12)
    requerente = models.ForeignKey(Requerente, on_delete=models.CASCADE)
    endereco_obra = models.ForeignKey(EnderecoObra, on_delete=models.CASCADE)
    area_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    area_construida = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True)
    data_alvara = models.DateField()
    resp_tecnico = models.ForeignKey(ResponsavelTecnico, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}/{1} - {2}".format(self.num_alvara, self.ano_alvara, self.requerente.nome_requerente)