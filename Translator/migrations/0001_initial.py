# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('family_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='translator',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Translator.user'),
        ),
    ]
