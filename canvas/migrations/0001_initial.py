# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 02:33
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CanvasItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('color', colorfield.fields.ColorField(max_length=18)),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]