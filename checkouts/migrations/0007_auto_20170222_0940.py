# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-22 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0006_auto_20170221_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='affiliate_manager_approved',
            field=models.NullBooleanField(),
        ),
    ]
