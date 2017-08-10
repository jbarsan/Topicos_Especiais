from django import forms
from .models import *


class CadastrarAlvaraForm(forms.Form):
    num_alvara = forms.IntegerField(unique=True, required=True)
    ano_alvara = forms.IntegerField(required=True)
    num_processo = forms.CharField(required=True)
    nome_requerente = forms.CharField(required=True)
    logradouro = forms.CharField(required=True)
    numero = forms.CharField(required=True)
    complemento = forms.CharField(required=False)
    bairro = forms.Select()
    cidade = forms.Select()
    area_terreno = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    area_construida = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    observacao = forms.Textarea()
    data_alvara = forms.DateField(required=True)
    resp_tecnico = forms.Select()

    def is_valid(self):
        valid = True

        if not super(CadastrarAlvaraForm, self).is_valid():
            self.adiciona_mensagem('Verifique todos os campos.')
            valid = False

        alvara = AlvaraConstrucao.objects.filter(num_alvara=self.cleaned_data["num_alvara"],
                                                 ano_alvara=self.cleaned_data["ano_alvara"])

        if alvara:
            adiciona_mensagem('Já existe um alvará cadastrado com esse número.')
            valid = False
        return valid


class CadastrarAutoForm(forms.Form):
    num_auto = forms.IntegerField(unique=True, required=True)
    ano_auto = forms.CharField(required=True)
    num_processo = forms.IntegerField(required=True)
    nome_requerente = forms.CharField(required=True)
    endereco_obra = forms.CharField(required=True)
    numero = forms.CharField(required=True)
    complemento = forms.CharField(required=False)
    bairro = forms.Select()
    cidade = forms.Select()
    area_terreno = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    area_construida = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    observacao = forms.Textarea()
    data_auto = forms.DateField(required=True)
    resp_tecnico = forms.Select()

    def is_valid(self):
        valid = True

        if not super(CadastrarAutoForm, self).is_valid():
            self.adiciona_mensagem('Verifique todos os campos.')
            valid = False

        auto = AlvaraConstrucao.objects.filter(num_alvara=self.cleaned_data["num_auto"],
                                                 ano_alvara=self.cleaned_data["ano_auto"])

        if auto:
            adiciona_mensagem('Já existe um auto de regularização cadastrado com esse número.')
            valid = False
        return valid


class CadastrarHabiteSeForm(forms.Form):
    num_habitese = forms.IntegerField(unique=True, required=True)
    ano_habitese = forms.CharField(required=True)
    num_processo = forms.CharField(required=True)
    nome_requerente = forms.CharField(required=True)
    endereco_obra = forms.CharField(required=True)
    numero = forms.CharField(required=True)
    complemento = forms.CharField(required=False)
    bairro = forms.Select()
    cidade = forms.Select()
    area_terreno = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    area_construida = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    observacao = forms.Textarea()
    data_auto = forms.DateField(required=True)
    resp_tecnico = forms.Select()

    def is_valid(self):
        valid = True

        if not super(CadastrarHabiteSeForm, self).is_valid():
            self.adiciona_mensagem('Verifique todos os campos.')
            valid = False

        habitese = AlvaraConstrucao.objects.filter(num_alvara=self.cleaned_data["num_habitese"],
                                                 ano_alvara=self.cleaned_data["ano_habitese"])

        if habitese:
            adiciona_mensagem('Já existe um Habite-se cadastrado com esse número.')
            valid = False
        return valid


def adiciona_mensagem(self, msg):
    errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
    errors.append(msg)
