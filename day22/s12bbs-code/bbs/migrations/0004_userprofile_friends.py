# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-11 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20160604_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='bbs.UserProfile'),
        ),
    ]
