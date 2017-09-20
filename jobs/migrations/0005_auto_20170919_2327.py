# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_examdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobclass',
            name='career_ladder_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobclass',
            name='exam_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobclass',
            name='occupational_category',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobclass',
            name='qualifications',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobclass',
            name='responsibilities',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobclass',
            name='skills',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]