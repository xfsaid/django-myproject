# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publish-time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='update-time')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tec_title', models.CharField(max_length=100)),
                ('tec_age', models.IntegerField(default=0)),
                ('tec_area', models.CharField(max_length=50)),
                ('tec_info', models.CharField(max_length=200)),
                ('tec_limit_price', models.FloatField(default=0)),
                ('tec_max_price', models.FloatField(default=0)),
                ('tec_evaluation_num', models.IntegerField(default=0)),
                ('tec_other_info', models.CharField(max_length=100)),
            ],
        ),
    ]