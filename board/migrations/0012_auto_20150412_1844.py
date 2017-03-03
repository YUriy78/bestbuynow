# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_auto_20150410_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='type',
        ),
        migrations.DeleteModel(
            name='TypeAd',
        ),
    ]
