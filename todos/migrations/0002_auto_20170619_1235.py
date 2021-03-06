# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 18:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=2)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
