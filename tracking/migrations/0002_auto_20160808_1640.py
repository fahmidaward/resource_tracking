# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-08 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deviceid',
            field=models.CharField(editable=False, max_length=32, unique=True),
        ),
    ]
