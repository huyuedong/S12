# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0004_userprofile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='bbs.UserProfile'),
        ),
    ]