# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170913_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendente',
            name='owner',
        ),
    ]
