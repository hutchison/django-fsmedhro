# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAir', '0002_auto_20170319_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='frage',
            name='Fragentext',
            field=models.TextField(blank=True, verbose_name='Frage'),
        ),
        migrations.AddField(
            model_name='frage',
            name='answerA',
            field=models.TextField(null=True, verbose_name='A'),
        ),
        migrations.AddField(
            model_name='frage',
            name='answerB',
            field=models.TextField(null=True, verbose_name='B'),
        ),
        migrations.AddField(
            model_name='frage',
            name='answerC',
            field=models.TextField(null=True, verbose_name='C'),
        ),
        migrations.AddField(
            model_name='frage',
            name='answerD',
            field=models.TextField(null=True, verbose_name='D'),
        ),
        migrations.AddField(
            model_name='frage',
            name='answerE',
            field=models.TextField(null=True, verbose_name='E'),
        ),
        migrations.AddField(
            model_name='frage',
            name='option1',
            field=models.TextField(blank=True, null=True, verbose_name='Option 1'),
        ),
        migrations.AddField(
            model_name='frage',
            name='option2',
            field=models.TextField(blank=True, null=True, verbose_name='Option 2'),
        ),
        migrations.AddField(
            model_name='frage',
            name='option3',
            field=models.TextField(blank=True, null=True, verbose_name='Option 3'),
        ),
        migrations.AddField(
            model_name='frage',
            name='option4',
            field=models.TextField(blank=True, null=True, verbose_name='Option 4'),
        ),
        migrations.AddField(
            model_name='frage',
            name='option5',
            field=models.TextField(blank=True, null=True, verbose_name='Option 5'),
        ),
        migrations.AddField(
            model_name='frage',
            name='scoreA',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frage',
            name='scoreB',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frage',
            name='scoreC',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frage',
            name='scoreD',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frage',
            name='scoreE',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='frage',
            name='Klausur',
        ),
        migrations.AddField(
            model_name='frage',
            name='Klausur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='QuestionAir.Klausur', verbose_name='Klausur'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='klausur',
            name='Fach',
        ),
        migrations.AddField(
            model_name='klausur',
            name='Fach',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='QuestionAir.Fach', verbose_name='Fach'),
            preserve_default=False,
        ),
    ]