# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-16 23:45
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0017_userprofile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='user_picture'),
        ),
    ]
