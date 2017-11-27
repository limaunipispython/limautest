# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-19 23:35
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0018_auto_20171117_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='/media/user_picture/Koala.jpg', null=True, upload_to='user_picture'),
        ),
    ]