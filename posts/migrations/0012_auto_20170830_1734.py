# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20170829_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'M'), ('Female', 'F')], max_length=128, null=True),
        ),
    ]