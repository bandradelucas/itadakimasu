# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-21 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20180621_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='served',
            field=models.BooleanField(default=False, verbose_name='Atendido?'),
        ),
    ]
