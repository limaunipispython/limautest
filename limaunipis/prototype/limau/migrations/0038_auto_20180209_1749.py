# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-09 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0037_auto_20180209_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default='5.00', max_digits=10),
        ),
    ]
