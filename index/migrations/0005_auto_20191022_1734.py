# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-22 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20191021_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='ImageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'imagetype',
            },
        ),
        migrations.AddField(
            model_name='images',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.ImageType'),
        ),
    ]