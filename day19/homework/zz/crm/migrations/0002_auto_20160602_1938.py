# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_', '可以查看'),), 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='class_list',
            field=models.ManyToManyField(blank=True, null=True, to='crm.ClassList', verbose_name='已报班级'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='日期'),
        ),
    ]