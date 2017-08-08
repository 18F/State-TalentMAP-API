# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 16:49
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='position_preferences',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text="JSON object containing filters representing a user's position preferences"),
        ),
    ]