# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-17 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xinjingshifangzhou', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='hero_content_wrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_header_name', models.CharField(max_length=100)),
                ('entry_header_title', models.CharField(max_length=200)),
                ('entry_header_content', models.CharField(max_length=500)),
                ('entry_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hero_icon_boxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(max_length=100)),
                ('entry_content', models.CharField(max_length=1000)),
                ('image_name_white', models.CharField(max_length=100)),
                ('image_name_grey', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='home_page_welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_header', models.CharField(max_length=100)),
                ('entry_content', models.CharField(max_length=1000)),
                ('image_welcome', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]