# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-18 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0029_userprofile_badge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='description of announcement', max_length=50)),
                ('text', models.TextField(default='write the announcement here')),
            ],
        ),
    ]
