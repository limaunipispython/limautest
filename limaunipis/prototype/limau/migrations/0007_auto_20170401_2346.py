# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0006_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurantcategory',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurantcategory',
            field=models.ManyToManyField(to='limau.RestaurantCategory'),
        ),
    ]