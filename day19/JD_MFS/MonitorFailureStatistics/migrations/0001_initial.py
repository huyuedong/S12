# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occ_time', models.DateField(verbose_name='日期')),
                ('str_time', models.DateTimeField(verbose_name='发生时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('time_consuming', models.TimeField(verbose_name='处理耗时')),
                ('fault_info', models.CharField(max_length=255, verbose_name='问题（故障）')),
                ('fault_ip', models.GenericIPAddressField(verbose_name='IP')),
                ('fault_status', models.CharField(choices=[('solved', '解决'), ('follow', '跟进'), ('unknown', '未知')], max_length=32, verbose_name='处理结果')),
                ('notify_person', models.CharField(max_length=64, verbose_name='通知人')),
                ('handle_person', models.CharField(max_length=64, verbose_name='处理人')),
                ('responsible_party', models.CharField(max_length=255, verbose_name='故障责任方')),
                ('memo', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'verbose_name': '监控故障报警统计',
                'verbose_name_plural': '监控故障报警统计',
            },
        ),
    ]
