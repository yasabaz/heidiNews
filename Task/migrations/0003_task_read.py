# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_auto_20170426_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
