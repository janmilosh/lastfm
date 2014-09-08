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
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=32)),
                ('lat', models.CharField(max_length=16)),
                ('lon', models.CharField(max_length=16)),
                ('timestamp', models.DateTimeField(verbose_name=b'timestamp')),
                ('user', models.ForeignKey(related_name=b'locations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
            bases=(models.Model,),
        ),
    ]
