# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170213_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]