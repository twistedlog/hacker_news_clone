# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0003_auto_20150724_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 24, 17, 47, 12, 713852), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsitem',
            name='modified',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.utcnow, auto_now=True),
            preserve_default=False,
        ),
    ]
