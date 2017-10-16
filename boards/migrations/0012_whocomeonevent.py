# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 13:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0011_auto_20171008_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoComeOnEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WhoComeOnEvent', to=settings.AUTH_USER_MODEL)),
                ('which_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WhoComeOnEvent', to='boards.Topic')),
            ],
        ),
    ]
