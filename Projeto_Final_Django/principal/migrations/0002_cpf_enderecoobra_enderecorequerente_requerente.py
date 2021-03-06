# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoObra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=20)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoRequerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=20)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Requerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_requerente', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('cpf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cpf_requerente', to='principal.CPF')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_requerente', to='principal.EnderecoRequerente')),
            ],
        ),
    ]
