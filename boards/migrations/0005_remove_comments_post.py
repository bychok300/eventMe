# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 11:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_comments_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
    ]
