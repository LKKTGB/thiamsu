# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 20:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thiamsu', '0006_auto_20171112_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='contributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]