# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20150412_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='status',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ad',
        ),
    ]
