# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0005_auto_20150724_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernewsitemtrack',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usernewsitemtrack',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
