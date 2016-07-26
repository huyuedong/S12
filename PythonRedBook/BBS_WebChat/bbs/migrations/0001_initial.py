# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-26 09:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('brief', models.CharField(blank=True, max_length=255, null=True, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='发布日期')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
                ('priority', models.IntegerField(default=1000, verbose_name='优先级')),
                ('head_img', models.ImageField(upload_to='articles', verbose_name='文章图片')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '已发布'), ('hidden', '隐藏')], default='published', max_length=32)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('brief', models.CharField(blank=True, max_length=255, null=True)),
                ('set_as_top_menu', models.BooleanField(default=False)),
                ('position_index', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': '版块',
                'verbose_name_plural': '版块',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.IntegerField(choices=[(1, '评论'), (2, '点赞')], default=1)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Article', verbose_name='所属文章')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_children', to='bbs.Comment', verbose_name='父评论')),
            ],
            options={
                'verbose_name': '评论/点赞',
                'verbose_name_plural': '评论/点赞',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('signature', models.CharField(blank=True, max_length=255, null=True)),
                ('head_img', models.ImageField(blank=True, null=True, upload_to='users')),
                ('friends', models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='bbs.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile', verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='category',
            name='admins',
            field=models.ManyToManyField(blank=True, to='bbs.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Category'),
        ),
    ]
