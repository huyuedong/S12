# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitorFailureStatistics', '0002_auto_20160531_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fault',
            name='memo',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='fault',
            name='time_consuming',
            field=models.CharField(max_length=64, verbose_name='处理耗时'),
        ),
    ]