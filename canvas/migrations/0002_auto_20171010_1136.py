# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvasitem',
            name='canvas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='canvas.Canvas'),
        ),
    ]
