# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170420_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(db_index=True, max_length=64),
        ),
    ]