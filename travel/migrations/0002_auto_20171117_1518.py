# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-17 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='location',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='user',
        ),
        migrations.AddField(
            model_name='visit',
            name='location_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='travel.Location'),
        ),
        migrations.AddField(
            model_name='visit',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
