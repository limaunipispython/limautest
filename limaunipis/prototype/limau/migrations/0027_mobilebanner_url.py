# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-08 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0026_auto_20180108_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilebanner',
            name='url',
            field=models.URLField(default='www.google.com'),
        ),
    ]
