# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=models.CharField(max_length=32),
        ),
    ]
