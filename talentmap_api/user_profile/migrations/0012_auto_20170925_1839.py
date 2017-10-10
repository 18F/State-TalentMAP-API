# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0014_auto_20170912_2139'),
        ('user_profile', '0011_auto_20170914_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='position.Grade'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='position.Skill'),
        ),
    ]