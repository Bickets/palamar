# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 11:08
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='ca_cert',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/kelepirci/palamar-dashboard/palamar/files'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='sites',
            name='client_cert',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/kelepirci/palamar-dashboard/palamar/files'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='sites',
            name='client_key',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/kelepirci/palamar-dashboard/palamar/files'), upload_to=b''),
        ),
    ]
