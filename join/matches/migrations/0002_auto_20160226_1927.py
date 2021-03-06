# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 19:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 26, 19, 27, 37, 412538, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchone', to='profiles.UserProfile'),
        ),
        migrations.AlterField(
            model_name='match',
            name='two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchtwo', to='profiles.UserProfile'),
        ),
    ]
