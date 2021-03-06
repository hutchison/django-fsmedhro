# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsmedhrocore', '0005_auto_20170412_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Fächer',
                'verbose_name': 'Fach',
            },
        ),
        migrations.RemoveField(
            model_name='dozent',
            name='studienabschnitt',
        ),
        migrations.RemoveField(
            model_name='dozent',
            name='studiengang',
        ),
        migrations.AlterField(
            model_name='dozent',
            name='titel',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dozent',
            name='vorname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dozent',
            name='fach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fsmedhrocore.Fach'),
        ),
    ]
