# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-21 02:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story_text',
            old_name='story_id',
            new_name='story',
        ),
    ]
