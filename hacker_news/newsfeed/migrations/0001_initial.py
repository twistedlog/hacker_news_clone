# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('hn_url', models.URLField()),
                ('posted_on', models.DateTimeField()),
                ('upvotes', models.IntegerField()),
                ('comments', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserNewsItemTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('news_item', models.ForeignKey(to='newsfeed.NewsItem')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
