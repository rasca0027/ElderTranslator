# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elder', '0002_auto_20160616_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='phone',
        ),
        migrations.AlterField(
            model_name='gesture',
            name='name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
