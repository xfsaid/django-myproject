# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-21 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20170822_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image_path',
            field=models.FileField(blank=True, upload_to='./upload/images/teachers'),
        ),
    ]
