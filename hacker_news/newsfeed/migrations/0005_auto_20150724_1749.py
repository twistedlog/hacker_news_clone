# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20150724_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernewsitemtrack',
            name='created',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.utcnow, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usernewsitemtrack',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 24, 17, 49, 32, 707749), auto_now=True),
            preserve_default=False,
        ),
    ]
