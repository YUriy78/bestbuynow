# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biduser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='biduser',
            name='status',
        ),
        migrations.DeleteModel(
            name='BidUser',
        ),
    ]
