# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-21 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0032_auto_20180121_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient_content',
            field=models.TextField(default='type your ingredients here, in <li> form'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='type a description of your recipe'),
        ),
    ]
