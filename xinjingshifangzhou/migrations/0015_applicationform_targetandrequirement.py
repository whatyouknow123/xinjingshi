# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-21 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xinjingshifangzhou', '0014_auto_20190421_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('age', models.BigIntegerField()),
                ('height', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TargetAndRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]