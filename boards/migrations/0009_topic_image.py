# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_auto_20171007_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
