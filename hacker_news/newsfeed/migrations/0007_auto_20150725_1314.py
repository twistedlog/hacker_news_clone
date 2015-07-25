# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0006_auto_20150725_1306'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usernewsitemtrack',
            unique_together=set([('user', 'news_item')]),
        ),
    ]
