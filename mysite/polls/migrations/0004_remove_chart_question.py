# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_chart_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='question',
        ),
    ]
