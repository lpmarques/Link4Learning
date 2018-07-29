# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180728_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='nome',
            new_name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='-', max_length=100),
        ),
    ]