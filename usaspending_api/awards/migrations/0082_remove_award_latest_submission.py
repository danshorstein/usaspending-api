# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-14 15:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0081_auto_20170413_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='latest_submission',
        ),
    ]