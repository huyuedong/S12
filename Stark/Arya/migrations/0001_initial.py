# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-25 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=128, unique=True, verbose_name='主机名')),
                ('key', models.TextField(verbose_name='KEY')),
                ('status', models.SmallIntegerField(choices=[(0, 'Waiting Approval'), (1, 'Accepted'), (2, 'Rejected')], default=0, verbose_name='主机状态')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='组名')),
                ('hosts', models.ManyToManyField(blank=True, to='Arya.Host', verbose_name='包含主机')),
            ],
        ),
    ]
