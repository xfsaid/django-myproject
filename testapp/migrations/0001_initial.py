# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-07 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usermane', models.CharField(max_length=30)),
                ('headimg', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]
