# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-21 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xinjingshifangzhou', '0016_auto_20190421_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('words', models.TextField()),
            ],
        ),
    ]