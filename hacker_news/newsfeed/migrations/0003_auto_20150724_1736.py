# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_auto_20150723_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='hn_url',
            field=models.URLField(null=True),
        ),
    ]
