# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('LinuxL1', 'Linux中高级'), ('LinuxL2', 'Linux架构师'), ('Linux51', 'Linux中高级(51网络)'), ('LinuxL251', 'Linux中高级+架构合成班(51网络)'), ('PythonDevOps', 'Python自动化开发'), ('PythonFullStack', 'Python高级全栈开发'), ('PythonDevOps51', 'Python自动化开发(51网络)'), ('PythonFullStack51', 'Python全栈开发(51网络)'), ('BigDataDev', '大数据开发课程'), ('Cloud', '云计算课程')], max_length=64, verbose_name='课程名')),
                ('class_type', models.CharField(choices=[('online', '网络班'), ('offline_weekend', '面授班(周末)'), ('offline_fulltime', '面授班(脱产)')], max_length=64, verbose_name='班级类型')),
                ('pay_type', models.CharField(choices=[('deposit', '订金/报名费'), ('tution', '学费'), ('refund', '退款')], default='deposit', max_length=64, verbose_name='费用类型')),
                ('paid_fee', models.IntegerField(default=0, verbose_name='费用数额')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='交款日期')),
            ],
            options={
                'verbose_name_plural': '交款纪录',
                'verbose_name': '交款纪录',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程', 'verbose_name_plural': '课程'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '客户', 'verbose_name_plural': '客户'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': '校区', 'verbose_name_plural': '校区'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='consultant',
            field=models.ForeignKey(help_text='谁签的单就选谁', on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='负责老师'),
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='客户'),
        ),
    ]
