# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='citations',
            field=models.CharField(default='', max_length=500),
        ),
    ]
