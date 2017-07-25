# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-25 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_gradesubjectmenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20, verbose_name='\u5e74\u7ea7\u7b49\u7ea7')),
                ('slug', models.CharField(max_length=20, verbose_name='\u7b49\u7ea7\u5730\u5740')),
                ('intro', models.CharField(max_length=50, verbose_name='\u7b49\u7ea7\u4ecb\u7ecd')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=20, verbose_name='\u79d1\u76ee\u540d\u79f0')),
                ('slug', models.CharField(max_length=20, verbose_name='\u79d1\u76ee\u5730\u5740')),
                ('intro', models.CharField(max_length=50, verbose_name='\u79d1\u76ee\u4ecb\u7ecd')),
                ('grade_level', models.ManyToManyField(to='homepage.Grade', verbose_name='\u6240\u5c5e\u5e74\u7ea7')),
            ],
        ),
    ]