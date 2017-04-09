# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-09 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0008_restaurant_starhtml'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128)),
                ('name_en', models.TextField(max_length=128)),
                ('description', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('picture_1', imagekit.models.fields.ProcessedImageField(upload_to='user_recipe_thumbnail')),
                ('picture_2', imagekit.models.fields.ProcessedImageField(upload_to='user_recipe_thumbnail')),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
                ('recipecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='limau.RecipeCategory')),
            ],
        ),
    ]
