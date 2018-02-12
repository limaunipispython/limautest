# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-11 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0040_auto_20180211_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_member',
            field=models.DecimalField(decimal_places=2, default='7.50', max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='discounted_member_price',
            field=models.DecimalField(decimal_places=2, default='50.00', max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='member_price_switch',
            field=models.BooleanField(default=False),
        ),
    ]
