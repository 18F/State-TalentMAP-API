# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_location_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='is_territory',
        ),
    ]
