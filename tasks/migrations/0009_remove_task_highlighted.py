# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20160101_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='highlighted',
        ),
    ]
