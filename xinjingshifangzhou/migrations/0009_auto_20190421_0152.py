# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-21 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xinjingshifangzhou', '0008_auto_20190421_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderwords',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='leaderwords',
            name='type',
            field=models.TextField(),
        ),
    ]