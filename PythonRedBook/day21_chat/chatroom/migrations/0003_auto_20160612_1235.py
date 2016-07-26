# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_loginuser_head_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='head_img',
            field=models.CharField(choices=[('head-1.png', '男士1'), ('head-3.png', '男士2'), ('head-2.png', '女士1')], default='head-1.png', max_length=30, verbose_name='头像'),
        ),
    ]