# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-31 02:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20170127_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='years',
            options={'verbose_name_plural': 'Years'},
        ),
    ]