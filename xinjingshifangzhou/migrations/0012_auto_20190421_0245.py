# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-21 02:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('xinjingshifangzhou', '0011_auto_20190421_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('current_image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyParter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('current_image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('current_image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='baseinfo',
            name='company_description',
            field=models.TextField(default=datetime.datetime(2019, 4, 21, 2, 45, 49, 833314, tzinfo=utc)),
            preserve_default=False,
        ),
    ]