# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180729_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='course',
        ),
        migrations.AddField(
            model_name='skill',
            name='course',
            field=models.ManyToManyField(to='core.Course'),
        ),
    ]