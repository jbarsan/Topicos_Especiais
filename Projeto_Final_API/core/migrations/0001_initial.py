# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 05:33
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(help_text='Matrícula do atendente', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='atendente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bairro', models.CharField(help_text='Nome do bairro', max_length=200, verbose_name='Nome do bairro')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
                'ordering': ('nome_bairro',),
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Descrição do cargo', max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(help_text='Informe o nome da cidade', max_length=100, verbose_name='Nome da cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], help_text='Informa o estado em que a cidade pertence', max_length=2, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ('nome_cidade',),
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField(help_text='Ano do documento a partir de 2013', validators=[core.models.valida_ano], verbose_name='Ano do documento')),
                ('num_processo', models.CharField(help_text='Número do processo no formato: 00.0000/0000', max_length=12, verbose_name='Número do processo')),
                ('end_obra', models.CharField(help_text='Endereço da obra', max_length=150, verbose_name='Endereço da obra')),
                ('num_residencia', models.CharField(help_text='Número do endereço, se não possuir insira "S/N"', max_length=20, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, help_text='Senão possuir complemento deixe em branco', max_length=150, null=True)),
                ('cep', models.CharField(blank=True, help_text='Cep no formato 00000-000', max_length=9, null=True)),
                ('area_terreno', models.DecimalField(decimal_places=2, help_text='Área do terreno no formato: 000.00', max_digits=10, verbose_name='Área do terreno')),
                ('area_construida', models.DecimalField(decimal_places=2, help_text='Área construída no formato: 000.00', max_digits=10, verbose_name='Área construída')),
                ('observacao', models.TextField(blank=True, help_text='Senão possuir observações deixe em branco', verbose_name='Observações')),
                ('data_documento', models.DateField(help_text='Data em que o documento foi assinado. YYYY-MM-DD', verbose_name='Data do documento')),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now, help_text='Data e hora do cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Requerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo do requerente', max_length=150, verbose_name='Nome do requerente')),
                ('cpf', models.CharField(help_text='C.P.F no formato: 000.000.000-00', max_length=14, unique=True, verbose_name='C.P.F')),
                ('telefone', models.CharField(help_text='Telefone Ex.: (00) 9 0000-0000 / (00) 0000-0000', max_length=16, verbose_name='Telefone')),
                ('endereco', models.CharField(help_text='Nome do logradouro', max_length=150, verbose_name='Endereço')),
                ('num_residencia', models.CharField(help_text='Número da casa, se não possuir insira "S/N"', max_length=20, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, help_text='Senão possuir complemento deixe em branco', max_length=150, null=True)),
                ('cep', models.CharField(blank=True, help_text='Cep no formato 00000-000', max_length=9, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now, help_text='Data e hora do cadastro')),
                ('bairro', models.ForeignKey(help_text='Bairro', on_delete=django.db.models.deletion.CASCADE, to='core.Bairro', verbose_name='Bairro')),
            ],
            options={
                'verbose_name': 'Requerente',
                'verbose_name_plural': 'Requerentes',
            },
        ),
        migrations.CreateModel(
            name='ResponsavelTecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo do responsável técnico', max_length=150)),
                ('cargo', models.ForeignKey(help_text='Cargo do responsável técnico', on_delete=django.db.models.deletion.CASCADE, to='core.Cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Responsável Técnico',
                'verbose_name_plural': 'Responsáveis Técnicos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='AlvaraConstrucao',
            fields=[
                ('documento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Documento')),
                ('numero', models.PositiveIntegerField(help_text='Número do documento', unique=True, validators=[core.models.valida_num], verbose_name='Número do documento')),
            ],
            options={
                'verbose_name': 'Alvará de Construção',
                'verbose_name_plural': 'Alvarás de Construção',
                'ordering': ('numero', 'ano'),
            },
            bases=('core.documento',),
        ),
        migrations.CreateModel(
            name='AutoRegularizacao',
            fields=[
                ('documento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Documento')),
                ('numero', models.PositiveIntegerField(help_text='Número do documento', unique=True, validators=[core.models.valida_num], verbose_name='Número do documento')),
            ],
            options={
                'verbose_name': 'Auto de Regularização',
                'verbose_name_plural': 'Autos de Regularização',
            },
            bases=('core.documento',),
        ),
        migrations.CreateModel(
            name='HabiteSe',
            fields=[
                ('documento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Documento')),
                ('numero', models.PositiveIntegerField(help_text='Número do documento', unique=True, validators=[core.models.valida_num], verbose_name='Número do documento')),
                ('alvara', models.ForeignKey(blank=True, help_text='Alvará associado, senão possuir deixe em branco', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AlvaraConstrucao', verbose_name='Alvará')),
                ('auto', models.ForeignKey(blank=True, help_text='Auto associado, senão possuir deixe em branco', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AutoRegularizacao', verbose_name='Auto')),
            ],
            options={
                'verbose_name': 'Habite-se',
                'verbose_name_plural': 'Habite-ses',
            },
            bases=('core.documento',),
        ),
        migrations.AddField(
            model_name='documento',
            name='bairro',
            field=models.ForeignKey(help_text='Bairro', on_delete=django.db.models.deletion.CASCADE, to='core.Bairro', verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='documento',
            name='requerente',
            field=models.ForeignKey(help_text='Requerente do documento', on_delete=django.db.models.deletion.CASCADE, to='core.Requerente', verbose_name='Requerente'),
        ),
        migrations.AddField(
            model_name='documento',
            name='resp_tecnico',
            field=models.ForeignKey(help_text='Responsável Técnico', on_delete=django.db.models.deletion.CASCADE, to='core.ResponsavelTecnico', verbose_name='Responsável técnico'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(help_text='Cidade em que o bairro pertence', on_delete=django.db.models.deletion.CASCADE, related_name='cidade', to='core.Cidade', verbose_name='Cidade'),
        ),
    ]
